#!/usr/bin/python3
"""
    LRUCache Module
"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Basic cache system using LRU algorithm.
      - Inherits from BaseCaching and is a caching system.

      - Put function:
        >> Must assign to the dictionary self.cache_data the 'item'
           value for the key 'key'.
        >> If 'key' or 'item' is None, this method should not do anything.
        >> If the number of items in self.cache_data is higher that
           BaseCaching.MAX_ITEMS:
           > you must discard the least recently used item (LRU algorithm)
           > you must print DISCARD: with the key discarded and
             following by a new line.

      - Get function:
        >> Must return the value in self.cache_data linked to key.
        >> If 'key' is None or if the 'key' doesn’t exist in self.cache_data,
           return 'None'.
    """

    def __init__(self):
        """
            initialize LRU cache
        """
        super().__init__()
        self.lru_queue = []  # lru: is least recently used.

    def put(self, key, item):
        """
            Add an item in cache.
            Args:
                key: of the dict.
                item: value of the key.

        """
        if key and item is not None:
            value = self.get(key)

        # If cache is full, discard least recently used item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.lru_queue.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

        # Add the new item
        self.cache_data[key] = item

        # Update LRU queue
        if key in self.lru_queue:
            self.lru_queue.remove(key)
        self.lru_queue.append(key)

    def get(self, key):
        """
            Get an item by key.
            Args:
                key: of the dict.
            Return:
                value of the key.

        """
        if key is not None and key in self.cache_data:
            # Update position in LRU queue
            self.lru_queue.remove(key)
            self.lru_queue.append(key)
            return self.cache_data.get(key)
        return None
