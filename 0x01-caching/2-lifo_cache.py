#!/usr/bin/env python3
"""The implementation of LIFOCache"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """The class implementation of LIFOCache
    that inherits from BaseCaching"""
    def __init__(self):
        """__init__ overloading"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """The implementation of the put for
        LIFOCache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.stack.append(key) if key not in self.stack else None
            if len(self.stack) > BaseCaching.MAX_ITEMS:
                key_to_pop = self.stack.pop(-2)
                del self.cache_data[key_to_pop]
                print(f"DISCARD: {key_to_pop}")

    def get(self, key):
        """Method to get the value of a given key"""
        return self.cache_data.get(key)
