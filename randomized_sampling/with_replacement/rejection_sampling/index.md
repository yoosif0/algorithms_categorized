R: range to sample from
F: fitting critteria
You sample from a `R` and only accept if what u sampled is in `F`. Otherwise reject

Works well when probability of `F/R` is high. Otherwise you'd reject a lot and waste time looping.

Situations when `F/R` is high:

- you sample a lot and do not want to pick the same sample twice. `F/R` is high because the probability of fitting criteria gets reduced the more u sample.
- `R >> F` from beginning (>> here means much bigger)
