# https://leetcode.com/problems/design-hashmap/description/

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = [-1 for i in range(1000001)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.l[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.l[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.l[key] = -1