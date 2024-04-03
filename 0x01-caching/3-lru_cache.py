#!/usr/bin/python3
"""
LRUCache
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ basic cache system using LRU algorithm """
    def __init__(self):
        """ initialize LRU cache """
        super().__init__()
        self.lru_queue = [] # lru: is least recently used.

    def put(self, key, item):
        """ add an item in cache """
        if key and item is not None:
            value = self.get(key)
            if value is None:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    if self.lru_queue:
                        lru_key = self.lru_queue.pop(0)
                        if lru_key in self.cache_data:
                            del self.cache_data[lru_key]
                            print("DISCARD: {}".format(lru_key))

            self.cache_data[key] = item
            self.lru_queue.append(key)

    def get(self, key):
        """ get an item by key """
        if key is not None and key in self.cache_data:
            self.lru_queue.remove(key)
            self.lru_queue.append(key)
            return self.cache_data.get(key)
        return None
