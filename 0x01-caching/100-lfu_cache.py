#!/usr/bin/env python3
"""Module implementation of the LFRU Caching
system"""


from collections import OrderedDict


BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """The class blueprint of the LFU
    Caching system"""
    def __init__(self):
        """The init overloading"""
        super().__init__()
        self.lfuTrack = OrderedDict()

    def put(self, key, item):
        """The method called put, that adds
        item to the data cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            # Keep track of frequency
            if key not in self.lfuTrack:
                self.lfuTrack[key] = 1
            else:
                self.lfuTrack[key] += 1
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Get the min value in lfuTrack
                # That corresponds with the minimum value, where
                # it does not track minimum value when the key is a new key.
                if self.lfuTrack[key] != 1:
                    min_val = min(self.lfuTrack.values())
                else:
                    min_val = min(list(self.lfuTrack.values())[:-1])
                keys_to_pop = [
                    k for k in self.lfuTrack.keys()
                    if self.lfuTrack[k] == min_val
                ]
                key_to_pop = keys_to_pop[0]
                del self.cache_data[key_to_pop]
                del self.lfuTrack[key_to_pop]
                print(f"DISCARD: {key_to_pop}")

    def get(self, key):
        """Method that implements the get ability of the
        LFU Caching"""
        if self.cache_data.get(key) is not None:
            self.lfuTrack[key] += 1
            self.lfuTrack.move_to_end(key)
            return self.cache_data.get(key)
        return None
