# v1 — The Autograd Engine

The first version of monktensor: a scalar automatic-differentiation engine and a tiny neural-network
library on top of it, trained to separate the two-moons dataset. It is the smallest project with the
deepest payoff — roughly a few hundred lines, but it demystifies how learning actually works.

## Goal

Build the four jobs of a framework on single numbers, where every operation and every gradient is visible:
represent a computation as a graph, run it forward, compute gradients automatically (backprop), and update
parameters to train a small classifier.

## Collaboration mode (important)

**v1 is learn-by-building. The implementation is written by hand, by Sameer.** The assistant's role here is
teacher and reviewer: guide the stack and the theory, explain plain-English-first then the precise terms,
scaffold, ask Socratic questions, review the code, and unblock. The assistant does **not** write the
engine's implementation. The [knowledge course](../../knowledge) carries the concepts; it deliberately
never shows the implementation (see [AUTHORING.md](../../knowledge/AUTHORING.md), rule 1).

## Milestones

`[ ]` not started · `[~]` in progress · `[x]` done

- `[ ]` **1. The scalar value type.** A value that wraps one number and remembers how it was made: its
  data, its gradient (starting at 0), its parent values, and which operation produced it.
- `[ ]` **2. Forward operations.** Add, multiply, power, and an activation (tanh or relu). Each builds the
  graph as it runs and knows its own local gradient rule (knowledge Unit 1).
- `[ ]` **3. The backward pass.** Topologically sort the graph, seed the output gradient at 1, walk in
  reverse applying local gradients, and accumulate where a value fans out (knowledge Unit 2).
- `[ ]` **4. The gradient check.** Verify backprop against finite-difference nudges within a small
  tolerance. This is the test that proves the engine works — write it early (knowledge 2.4).
- `[ ]` **5. The neural-net library.** Neuron, then Layer, then MLP, with a `parameters()` method that
  gathers all the learnable values (knowledge Unit 3).
- `[ ]` **6. Loss and the training loop.** A loss (hinge/max-margin or binary cross-entropy) plus a little
  L2, and the loop: forward, zero gradients, backward, step (knowledge Unit 4).
- `[ ]` **7. Train make_moons.** Fit the two-moons dataset, then plot the decision boundary curving cleanly
  between the crescents (knowledge 4.1, 4.5).
- `[ ]` **8. Repo hygiene.** Tests (including the gradient check), a README with a usage example, and a
  notebook or script that produces the decision-boundary plot.

## Definition of done

The net separates make_moons; the gradient check passes; the README explains backprop in plain English;
and a notebook shows the decision boundary. Tests + a benchmark/plot + a real README = the senior-repo bar.

## Stack (provisional, pending the stack discussion)

- **Language:** Python. The scalar engine stays pure Python so every operation is visible; numpy is allowed
  only for the toy dataset and plotting.
- This will be confirmed in the dedicated stack discussion before implementation begins.

## How the course maps to this

Each milestone has matching lessons in the [knowledge course](../../knowledge): Foundations (the math),
Unit 1 (graph + local gradients), Unit 2 (backprop + gradient check), Unit 3 (neuron → MLP), Unit 4
(loss → training loop). Read the unit, then write the milestone.
