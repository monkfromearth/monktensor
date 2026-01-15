# Authoring the monktensor knowledge course

How every unit and lesson in `knowledge/` is written. Read this before adding or editing a lesson.
The point of this file is that the course stays one voice and one set of decisions, no matter who
(or which chat) writes the next unit.

---

## 1. The one rule that overrides everything

**This is knowledge, not documentation.** The course teaches the *concepts* a reader needs in order to
build monktensor themselves. It never shows monktensor's implementation.

- Teach the idea, the math, and worked numeric examples.
- NEVER write the engine: no `Value` class, no `_backward` closures, no layer/optimizer source, no
  "here's the code, copy it." If a page hands over the implementation, it has become documentation and
  failed its job.
- The line: explain backprop as *topological sort + chain rule with accumulation*, with a worked graph
  by hand. Do **not** write the function that does it. The reader writes the code; that is where the
  understanding sticks.
- Tiny illustrative snippets that are NOT the framework (e.g. a finite-difference check in plain Python,
  three lines) are allowed sparingly. The test: would copying this snippet build monktensor for them? If
  yes, cut it.

## 2. Voice

Inherits the workspace `plain-english` rule.

- **Plain words first, the precise term second.** Say the real-world meaning, then name the term once,
  in parentheses or a trailing clause. "How much the output moves when you nudge the input (the derivative)."
- **Calm, curious, smart-friend.** Never lecture-y, never hype. No emojis, ever.
- **Concrete over abstract.** Lead with an analogy or a worked number, not a definition.
- **Worked numeric examples over proofs.** The house style is "nudge it by 0.001 and watch the number
  move." This mirrors how the gradient-check will feel later. Formal math can ride alongside, but the
  numeric intuition leads.
- **One technical term per idea, max.** If a sentence has three pieces of jargon, rewrite it.
- No em-dash-as-AI-tell overuse; vary sentence shape.

## 3. Lesson structure

Each lesson is one `.astro` page using these pieces, in this order:

1. Frontmatter: import `LessonLayout`, `LessonHeader`, `LessonNav`, and whatever boxes/demos it uses.
2. `<LessonLayout title lessonNumber section>` wrapping everything.
3. `<LessonHeader lessonNumber title description>` with 1-2 `<TagBadge>` (one topic tag + a read-time).
4. 3-6 `<section class="mb-14">` blocks. Typical rhythm per section: **hook/analogy → the concept →
   a worked example → an `InsightBox`** that names the takeaway.
5. Optional "What it is NOT" section (cross-out cards) to kill misconceptions.
6. Optional `<ExerciseBox>` — something to work by hand.
7. A "Key takeaways" section: 3 numbered points.
8. `<LessonNav prevHref prevLabel nextHref nextLabel>` — chain to the neighbours.

Keep a lesson to roughly a 9-12 minute read. If it is longer, split it.

## 4. Components

| Component | Use for |
|-----------|---------|
| `LessonLayout` | page shell (nav bar, fonts, footer). Required. |
| `LessonHeader` | title block + tags. Required. |
| `LessonNav` | prev/next at the bottom. Required. |
| `InsightBox` | the coral "remember this" callout. The takeaway of a section. |
| `ExerciseBox` | green "work it by hand" prompt. |
| `Formula` | centered math display (styled HTML, no KaTeX). Use `<span class="var">` / `<span class="op">`. |
| `StepNumber` | numbered circle for ordered walkthroughs. |
| `TagBadge` | small pill: `concepts` · `intuition` · `math` · `exercise` · `glossary` · `links`. |
| animated demos (`demos/`) | see the animation policy below. |

## 5. Visual constraints

- Palette is the `mt-*` Tailwind tokens only (warm beige `mt-bg`, coral `mt-accent`, plus
  `mt-lav` / `mt-blue` / `mt-rose` / `mt-green` / `mt-amber`). No raw hex in pages, no off-palette colors.
- Fonts: Figtree (sans) + JetBrains Mono (code/numbers). Loaded in the layout.
- Code blocks are dark (`#1E1B29`, the monktensor Shiki theme) and used sparingly — only for math or a
  non-framework illustration, per rule 1.
- **No emojis anywhere.**
- Every internal link and asset path goes through `import.meta.env.BASE_URL` (the site is served under
  `/monktensor/`). Hardcoding `/foundations/...` breaks on GitHub Pages.
- Brand assets (`logo.svg`, etc.) must exist in `knowledge/public/` — Astro serves that dir, not the
  repo-root `public/`.

## 6. Animation policy (GSAP)

Motion has to *teach*, or it doesn't ship.

- **Meaningful only.** Animate to make visible something a static page can't: a quantity changing, rates
  multiplying, a slope, a step downhill, gradient flowing backward. Never animate for polish, entrance
  flair, or decoration.
- **The test:** "does seeing it move explain the idea better than a sentence?" If no, use a sentence.
- **Interactive beats autoplay.** Prefer demos the reader drives (drag a value, watch the dependent
  value respond) over things that just play. Understanding comes from *they* moved it.
- **One demo per lesson, max.** A lesson is prose with a single illuminating interaction, not a toy box.
- **Respect `prefers-reduced-motion`.** If the user asked for less motion, show the final/static state
  and skip tweens. Every demo must still make sense with motion off.
- **Self-contained components.** Each demo is one file in `src/components/demos/`, owns its markup and
  its client `<script>` (GSAP imported there), and is scoped so multiple instances don't collide
  (`querySelectorAll` over a root class, never global ids).
- **Cheap.** No layout thrash; animate transforms/opacity and text content, not expensive properties.
  Demos are client-only (the `<script>` runs in the browser, not at build).

Current demos:
- `MultiplyNudgeDemo` — drag `a`, watch `c = a x b` move `b` times as fast. Shows `dc/da = b`. (Lesson 0.1, 0.3 idea.)
- `SlopeNudgeDemo` — drag `x` on a curve, watch the tangent slope. Shows a derivative as steepness. (Lesson 0.3.)
- `GearsDemo` — three gears; rates multiply down the chain (x3 then x2 = x6). Shows the chain rule. (Lesson 0.5.)

## 7. Adding a lesson — checklist

1. File: `src/pages/<unit>/<slug>.astro`. Units: `foundations`, `graph`, `backprop`, `networks`,
   `training`, `beyond`. Glossary is `src/pages/glossary.astro`.
2. Follow the structure in §3, the voice in §2, the one rule in §1.
3. Wire `LessonNav` to the previous and next lessons (check both neighbours' hrefs).
4. If it earns one, add a single meaningful demo per §6.
5. Update `src/pages/index.astro`: lesson row, unit lesson count, and flip the unit card from locked to
   active when the unit is complete. Update the header lesson total.
6. `bun run build` must pass before the lesson is "done."

## 8. The curriculum (current plan)

- **0 Foundations** (5): what a framework is · learning as fitting · derivatives · gradients · chain rule
- **1 The Computation Graph** (4): computation as a graph · the forward pass · parameters vs activations · local gradients
- **2 Backpropagation** (4): the backward pass · fan-out & accumulation · topological order · gradient checking (and why not finite differences)
- **3 Neural Networks** (3): the neuron · layers & the MLP · activations
- **4 Training** (5): the task & data · loss functions · gradient descent & SGD · initialization & regularization · the training loop
- **5 Beyond v1** (2): scalars to tensors · lazy evaluation & kernel fusion
- **Glossary** — every term, plain English then precise.
