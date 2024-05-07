#!/usr/bin/env python3
"""Module implementation of FIFOCache class"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """The class implementation of the
    FIFOCache"""
    def __init__(self):
        """Overloading the parent class init class"""
        super().__init__()
        self.keyTrack = []

    def put(self, key, item):
        """Method to define how to put items into the
        cache data"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.keyTrack.append(key) if key not in self.keyTrack else None
            if len(self.keyTrack) > BaseCaching.MAX_ITEMS:
                key_to_discard = self.keyTrack.pop(0)
                del self.cache_data[key_to_discard]
                print(f"DISCARD: {key_to_discard}")

    def get(self, key):
        """Method to get the value of a given key"""
        return self.cache_data.get(key)
