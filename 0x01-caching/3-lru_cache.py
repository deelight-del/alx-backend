#!/usr/bin/env python3
"""The module implementation of LRU caching"""


BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """Class implementation of LRUCache"""
    def __init__(self):
        """The init method of the implemented class"""
        super().__init__()
        self.lruTrack = []

    def put(self, key, item):
        """The put method of the lru cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.lruTrack.append(key) if key not in self.lruTrack else None
            if len(self.lruTrack) > BaseCaching.MAX_ITEMS:
                key_to_pop = self.lruTrack.pop(0)
                del self.cache_data[key_to_pop]
                print(f"DISCARD: {key_to_pop}")

    def get(self, key):
        """The get method of the LRU cahcing"""
        if self.cache_data.get(key) is not None:
            self.lruTrack.remove(key)
            self.lruTrack.append(key)
            return self.cache_data.get(key)
        return None
