class MyHashSet:

    def __init__(self):
        self.hashSet = []
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashSet.append(key)
        
        return

    def remove(self, key: int) -> None:
        for i, val in enumerate(self.hashSet):
            if val == key:
                self.hashSet.pop(i)
                return
        
        return

    def contains(self, key: int) -> bool:
        for val in self.hashSet:
            if val == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)