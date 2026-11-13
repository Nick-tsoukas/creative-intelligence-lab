import { test, expect } from '@playwright/test';
import { fileURLToPath, pathToFileURL } from 'node:url';

const path = fileURLToPath(new URL('./index.html', import.meta.url));

test.beforeEach(async ({ page }) => {
  await page.goto(pathToFileURL(path).href);
});

test('opens with just first study visible and a usable document title', async ({ page }) => {
  await expect(page).toHaveTitle(/Perception Workbench/);
  await expect(page.getByRole('tabpanel', { name: /Visual weight/i })).toBeVisible();
  await expect(page.locator('#panel-grouping')).toBeHidden();
  await expect(page.locator('#panel-color')).toBeHidden();
});

test('tablist supports arrows, Home, End, and focus', async ({ page }) => {
  const first = page.getByRole('tab', { name: /Visual weight/ });
  await first.focus();
  await first.press('ArrowRight');
  await expect(page.getByRole('tab', { name: /Grouping/ })).toBeFocused();
  await expect(page.locator('#panel-grouping')).toBeVisible();
  await page.keyboard.press('End');
  await expect(page.getByRole('tab', { name: /Color context/ })).toBeFocused();
  await expect(page.locator('#panel-color')).toBeVisible();
  await page.keyboard.press('Home');
  await expect(first).toBeFocused();
});

test('variants update without changing experimental text', async ({ page }) => {
  const stage = page.locator('#hierarchy-stage');
  const content = await stage.innerText();
  for (const variant of ['single', 'balanced', 'competing']) {
    await page.locator('#hierarchy-mode').selectOption(variant);
    await expect(stage).toHaveAttribute('data-mode', variant);
    expect(await stage.innerText()).toBe(content);
  }
});

test('records each answer and resets in-tab data', async ({ page }) => {
  await page.getByRole('button', { name: /Record current observation/ }).click();
  await expect(page.locator('#result')).toContainText(/Choose an observation first/);
  await page.locator('input[name="hierarchy-answer"][value="headline"]').check();
  await page.getByRole('button', { name: /Record current observation/ }).click();
  await expect(page.locator('#result')).toContainText('1 observation');
  await page.getByRole('button', { name: /Clear observations/ }).click();
  await expect(page.locator('#result')).toContainText('Observations cleared.');
  await expect(page.locator('input[name="hierarchy-answer"]:checked')).toHaveCount(0);
});

test('center color patches are identical while surrounds change', async ({ page }) => {
  await page.locator('#tab-color').click();
  const patchColors = await page.locator('.patch').evaluateAll(els => els.map(el => getComputedStyle(el).backgroundColor));
  expect(patchColors).toHaveLength(2);
  expect(patchColors[0]).toEqual(patchColors[1]);
  const before = await page.locator('.color-field').evaluateAll(els => els.map(el => getComputedStyle(el).backgroundColor));
  expect(before[0]).not.toEqual(before[1]);
  await page.locator('#color-mode').selectOption('matched');
  const after = await page.locator('.color-field').evaluateAll(els => els.map(el => getComputedStyle(el).backgroundColor));
  expect(after[0]).toEqual(after[1]);
});

for (const size of [{width:1280,height:800},{width:390,height:844},{width:320,height:640}]) {
  test('no body horizontal overflow at ' + size.width, async ({ page }) => {
    await page.setViewportSize(size);
    for (const tab of ['hierarchy','grouping','color']) {
      await page.locator('#tab-'+tab).click();
      const state = await page.evaluate(() => ({
        contentWidth:document.documentElement.scrollWidth,
        viewportWidth:document.documentElement.clientWidth
      }));
      expect(state.contentWidth, tab+' at '+size.width).toBeLessThanOrEqual(state.viewportWidth);
    }
  });
}

test('reduced-motion setting is queryable', async ({ page }) => {
  await page.emulateMedia({ reducedMotion:'reduce' });
  expect(await page.evaluate(() => matchMedia('(prefers-reduced-motion: reduce)').matches)).toBe(true);
});
