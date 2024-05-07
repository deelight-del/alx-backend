#!/usr/bin/env python3
"""This module implements a BaseCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """The class definiton of BasicCache"""
    def put(self, key, item):
        """Method to put a given item, with key
        into the cache attribute"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Method to get the item in a cache using
        the key"""
        return self.cache_data.get(key)
