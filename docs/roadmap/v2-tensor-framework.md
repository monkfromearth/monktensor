# v2 — The Tensor Framework

Once v1 works and the ideas are solid, v2 climbs from a teaching engine toward a real framework: tensors
for speed, then a lazy graph and a fusing compiler for the parts that separate a clone from the genuine
article. Inspired by tinygrad's balance of simplicity and capability.

## Goal

Keep the autograd logic from v1 (it doesn't change) and make it practical and fast: process arrays instead
of single numbers, defer computation so the whole graph can be optimized, and fuse operations into tight
kernels.

## Collaboration mode

v2 is research-heavy, so the mode shifts to pairing: working together on design and code, not the
teach-only stance of v1.

## Phases

`[ ]` not started · `[~]` in progress · `[x]` done

- `[ ]` **1. Tensor-valued autograd.** Replace scalars with n-dimensional arrays: broadcasting, matrix
  multiply, and the three operation families tinygrad reduces everything to — elementwise, reduction, and
  movement (reshape/transpose). The chain rule and accumulation are unchanged; values become arrays
  (knowledge 5.1).
- `[ ]` **2. Lazy evaluation.** Operations record into an op graph instead of computing immediately; nothing
  runs until a result is requested (`.realize()`) (knowledge 5.2).
- `[ ]` **3. Kernel fusion.** With the whole graph visible, fuse chains of operations into single passes over
  memory — the genuinely senior, least-cloned part. Applies to the backward pass too (knowledge 5.2).
- `[ ]` **4. Rigor.** Gradient-check against PyTorch; benchmark fused vs unfused. Demo: train MNIST, then a
  mini-GPT with attention built from scratch.

## Definition of done

Tensor autograd matches PyTorch gradients on real layers; the lazy + fused path measurably beats the naive
path; and the framework trains MNIST and a mini-GPT end to end.

## Paper potential — an honest note

A from-scratch framework is a superb learning artifact but rarely a novel paper in itself. The paper-aimed
bets in the wider portfolio are vector search and quantization; monktensor is the on-ramp that makes those
implementable with real understanding. Keep v2's ambition about craft and clarity, not a publication.
