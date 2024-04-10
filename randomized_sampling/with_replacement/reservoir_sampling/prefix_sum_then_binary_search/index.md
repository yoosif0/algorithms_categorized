```python
pre = list(accumulate(a, initial=0))
rnd = random.uniform(0, self.pre[-1])
return bisect.bisect_left(self.pre, rnd) - 1



```
