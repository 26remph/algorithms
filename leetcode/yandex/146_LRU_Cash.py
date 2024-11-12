class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}

    def get(self, key: int) -> int:
        if key in self.d:
            val = self.d[key]
            del self.d[key]
            self.d[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.d.get(key, None):
            del self.d[key]
        elif len(self.d) >= self.capacity:
            evict_key = next(iter(self.d))
            del self.d[evict_key]

        self.d[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 0)
    lru.put(2, 2)
    lru.get(1)
    lru.put(3, 3)
    lru.get(2)
    lru.put(4, 4)
    lru.get(1)
    lru.get(3)
    lru.get(4)
