class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.data.append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.data:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        to_remove = None
        for k, v in self.data:
            if k == key:
                to_remove = (k, v)
                break
        if to_remove:
            self.data.remove(to_remove)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)