class MyHashSet:
    def __init__(self):
        self.a = [False for _ in range(1000001)]

    def add(self, key: int) -> None:
        self.a[key] = True

    def contains(self, key: int) -> bool:
        return self.a[key]

    def remove(self, key: int) -> None:
        self.a[key] = False
