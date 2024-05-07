#!/usr/bin/env python3
"""The module for implementing a Most recently
used caching system."""


BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """The class blueprint of MRUCache"""
    def __init__(self):
        """The init method overloading of the parent
        class"""
        super().__init__()
        self.mruTrack = []

    def put(self, key, item):
        """The implementation of the put method
        of the MRU Cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.mruTrack.append(key) if key not in self.mruTrack else None
            if len(self.mruTrack) > BaseCaching.MAX_ITEMS:
                key_to_pop = self.mruTrack.pop(-2)
                del self.cache_data[key_to_pop]
                print(f"DISCARD: {key_to_pop}")

    def get(self, key):
        """Method to implement the get method"""
        if self.cache_data.get(key) is not None:
            self.mruTrack.remove(key)
            self.mruTrack.append(key)
            return self.cache_data.get(key)
        return None
