# Research 007 — Cinematic Image Language for Digital Experiences

**Access date:** 2026-11-11. **Source status:** official museum, gallery, filmmaking and motion-designer accounts reviewed online. This is **not** a full viewing of films, a photography book, or a live interactive UX test.

## Thesis
Cinematic design is not synonymous with black backgrounds, giant photos, slow scroll or expensive animation. It is a way of **allocating attention over time**: framing, light, lens, pacing, visual metaphor, and the order in which evidence becomes visible.

The test for transferring film language to a website is not "Does it feel like a film?" but "Does this visual method communicate the subject and leave the visitor in control?"

## Study A — Hiroshi Sugimoto: a repeated frame with infinite variation
**Institutional evidence:** Singapore Art Museum's Seascapes overview: https://www.singaporeartmuseum.sg/Art-Events/Exhibitions/Hiroshi-Sugimoto
**Other museum record:** https://hirshhorn.si.edu/explore/in-depth-hiroshi-sugimoto/

**FACT:** The museum describes Sugimoto's Seascapes as sharing a centered sea/sky horizon, varied by subtle differences of light, weather and atmosphere. The Hirshhorn discusses his minimal photographs across seascapes, theaters and architecture.

**INTERPRETATION:** A repeated visual structure does not require identical emotional character. Constraint can make nuance visible. The fixed horizon creates a constant comparison field so minute shifts in atmosphere become the subject.

**Transfer hypothesis:** A digital archive or artist gallery could maintain a stable framing system while letting image, color, scale and light express each subject. The *same frame* can allow differences to matter.

**Failure mode:** Cropping every performance photo to a rigid central horizon would erase faces, instruments, gestures and composition. Uniform card grids are not automatically artistic.

**Exercise:** Compare three gallery mockups with identical media: (1) identical crops, (2) art-directed varied crops, (3) fixed frame with adaptable focal positioning. Compare the emotional result and visibility of essential subject matter.

## Study B — Gregory Crewdson: staging as narrative construction
**Photography institution:** https://www.icp.org/browse/archive/constituents/gregory-crewdson
**Museum exhibition context:** https://www.taubmanmuseum.org/gregory-crewdson-eveningside

**FACT:** The International Center of Photography describes Crewdson's elaborately staged scenes and cinematic lighting, often produced with large support crews. The Taubman Museum describes the use of constructed environments, sets, interiors and lighting in his series.

**INTERPRETATION:** A compelling photograph may be a wholly constructed narrative environment rather than simply an attractive photograph. Details in the background can suggest a life or event without explicit exposition.

**Transfer hypothesis:** The *selection, cropping, lighting and sequencing* of real authorized imagery can tell a coherent story about a product's users. A branded website should not depend on generic people-at-laptops stock images when authentic subject matter is available.

**Failure mode:** Elaborately fabricated scenes may feel inauthentic or exploit the audience; production value does not substitute for accurate representation.

## Study C — Cinematography: visual rhythm is more than transitions
**Practitioner interview, American Society of Cinematographers:** https://staging.ascmag.com/articles/darius-khondji-cinematic-rhythms
**BFI educational guide:** https://www.bfi.org.uk/commercial-partnerships-consultancy/bfi-enterprise-news-highlights/how-shoot-high-quality-smartphone-videos-5-easy-steps

**FACT / PRACTITIONER ACCOUNT:** In the ASC interview, Darius Khondji describes creative rhythms as connected to camera movement, color, lighting and the tempo of a scene; the article also discusses Bong Joon-ho's emphasis on rhythm beyond editing alone. BFI recommends planning shots and backgrounds, watching smoothness and framing, and attending to sound and light.

**INTERPRETATION:** Web motion should have a narrative reason and consistent pacing. Uniform fade-up animations on every card are a motion preset, not an art-directed sequence.

**Transfer hypothesis:** Use a motion score: quiet arrival → focused reveal → purposeful interaction → unambiguous completion. Reserve dramatic transitions for storytelling moments, not routine buttons and forms.

**Failure mode:** A dramatic full-screen transition after every navigation creates friction, especially for returning visitors.

## Study D — Motion title design: the concept before the finish
**Practitioner interview:** https://motionographer.com/2022/06/28/project-breakdown-with-imaginary-forces/
**Process account:** https://motionographer.com/2024/06/11/the-dark-matter-title-sequence-how-we-created-it-three-times/
**Motion design case study:** https://motionographer.com/2020/05/13/spider-man-says-its-not-how-big-your-title-sequence-is-its-how-you-use-it-all-about-perception/

**FACT / CREATOR ACCOUNTS:** Motion designers describe distinguishing a strong central idea from highly polished visuals. The Dark Matter title team reports exploring multiple concepts before selecting a puzzle-box metaphor that reflected the story. A Spider-Man: Homecoming credits case describes scanning physical art-making techniques into a digital animation pipeline.

**INTERPRETATION:** The strongest transfer is the **concept-to-form relationship**, not camera movement, frame rate, or the specific art style. Physical texture and imperfect surfaces can communicate appropriate subject matter, but they can also become decorative nostalgia.

**Transfer hypothesis:** Design a homepage sequence with a single concept that becomes clearer through scrolling or interaction; explain the concept in one sentence without using aesthetic jargon.

**Failure mode:** A beautiful sequence that makes the visitor wait to understand what the product does is a failed homepage hero.

## Accessible motion and user agency
**W3C WCAG 2.2 SC 2.3.3 (AAA), official guide:** https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions

**FACT:** This criterion addresses nonessential motion animation triggered by interaction, which users must be able to disable. W3C cites CSS `prefers-reduced-motion` among sufficient techniques. The criterion is **AAA**, not a blanket AA requirement; other WCAG motion, pause and flashing provisions may apply depending on behavior.

**Design requirement for our experiments:** essential content remains available without motion. No scroll-locking as a necessary step to read product facts. Avoid unsolicited sound. Specify what happens on interruption, back navigation, reduced motion and low-powered devices.

## Cinematic art-direction decision matrix

| Subject | Potentially useful technique | User benefit to test | Failure condition |
|---|---|---|---|
| Emotional narrative / brand launch | singular scene, controlled light, paced reveal | remembrance and comprehension | task and CTA delayed |
| Artist imagery | original photography, deliberate crop, authentic stage light | recognition and identity | faces cropped or misrepresented |
| Repeated gallery | consistent rhythm with intentional focal variation | comparison and exploration | every image forced into wrong composition |
| Software dashboard | quiet framing, semantic hierarchy, concise transitions | faster task navigation | theatrical animation creates delay |
| Educational story | sequence of distinct visual chapters | improved understanding | too much animation obscures content |

## Reading queue, not yet completed
- Bruce Block, *The Visual Story* (3rd ed.) — publisher synopsis reviewed previously, not full text.
- Blain Brown, *Cinematography: Theory and Practice* — QUEUED.
- David Bordwell & Kristin Thompson, *Film Art: An Introduction* — QUEUED.
- Walter Murch, *In the Blink of an Eye* — QUEUED.
- John Berger, *Ways of Seeing* — QUEUED.

## Next work
Create a rights-safe storyboard demonstrating three kinds of rhythm (still, cinematic, operational) with original geometric and photographic-placeholder imagery. For actual Faneqo mockup direction later, review licensed real artist images and current live homepage content, not arbitrary stock images.

**Evidence notice:** Museum/practitioner statements are sourced; design transfers and predicted benefits are hypotheses. No user performance outcomes were measured.
