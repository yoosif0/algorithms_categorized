Pick number from 0 to n, then 0 to n-1, then 0 to n-2, etc.

```python
def shuffle(self) -> list[int]:
    for i in range(len(self.a) - 1, -1, -1):
        j = random.randint(0, i)
        self.a[i], self.a[j] = self.a[j], self.a[i]
    return self.a
```
