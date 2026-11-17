"""Synthetic capture validation, not model efficacy or product visual QA."""
import importlib.util
import struct
import tempfile
import unittest
import zlib
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/elite-ux-director/scripts/check_capture.py'
spec = importlib.util.spec_from_file_location('capture_check', SCRIPT)
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)


def png(w=80, h=160, blank_tail=False, filter_type=0, rgb=False):
    channels = 3 if rgb else 4
    previous = bytes(w * channels)
    rows = []
    for y in range(h):
        row = bytearray()
        for x in range(w):
            color = (0, 0, 0) if blank_tail and y > h // 3 else ((x * 13 + y * 7) % 256, (x * 9 + y * 19) % 256, (x * 3 + y * 11) % 256)
            row.extend(color if rgb else (*color, 255))
        encoded = bytearray()
        for i, value in enumerate(row):
            a = row[i - channels] if i >= channels else 0
            b = previous[i]
            c = previous[i - channels] if i >= channels else 0
            predictor = (0, a, b, (a + b) // 2, tool.paeth(a, b, c))[filter_type]
            encoded.append((value - predictor) & 255)
        rows.append(bytes([filter_type]) + encoded)
        previous = row
    def chunk(tag, payload):
        return struct.pack('>I', len(payload)) + tag + payload + struct.pack('>I', zlib.crc32(tag + payload))
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2 if rgb else 6, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(b''.join(rows))) + chunk(b'IEND', b''))


class CaptureTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'shot.png'

    def test_all_browser_png_filters(self):
        for rgb in (False, True):
            for filt in range(5):
                with self.subTest(rgb=rgb, filter=filt):
                    self.path.write_bytes(png(filter_type=filt, rgb=rgb))
                    self.assertEqual(tool.inspect(self.path, 80, 160)['status'], 'NO_AUTOMATED_CONCERN')

    def test_black_tail_requires_review(self):
        self.path.write_bytes(png(blank_tail=True))
        result = tool.inspect(self.path)
        self.assertEqual(result['status'], 'REVIEW_REQUIRED')
        self.assertGreater(result['flat_tail_rows'], 100)

    def test_wrong_capture_scope(self):
        self.path.write_bytes(png())
        with self.assertRaisesRegex(ValueError, 'Height'):
            tool.inspect(self.path, 80, 400)

    def test_corrupt_or_truncated_file(self):
        for blob in (png()[:-9], b'not an image', png()[:-17] + b'bad' + png()[-14:]):
            self.path.write_bytes(blob)
            with self.assertRaises(ValueError):
                tool.inspect(self.path)

    def test_huge_image_rejected_before_decode(self):
        blob = bytearray(png())
        blob[16:24] = struct.pack('>II', 100000, 100000)
        blob[29:33] = struct.pack('>I', zlib.crc32(blob[12:29]))
        self.path.write_bytes(blob)
        with self.assertRaisesRegex(ValueError, 'bounds'):
            tool.inspect(self.path)

    def test_legitimate_sparse_dark_image_is_not_a_quality_failure(self):
        self.path.write_bytes(png(blank_tail=True))
        result = tool.inspect(self.path)
        self.assertTrue(result['visual_inspection_required'])
        self.assertNotEqual(result['status'], 'INVALID')


if __name__ == '__main__':
    unittest.main()
