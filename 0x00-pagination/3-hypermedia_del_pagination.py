#!/usr/bin/env python3
"""

Deletion-resilient hypermedia pagination

"""


import csv
import math
from typing import Dict, List


class Server:
    """
        Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary containing hypermedia pagination
        information for the dataset.

        Arguments:
            index: An integer representing the start index of the..
            current page (default is None).
            page_size: An integer representing the number of items..
            per page (default is 10).

        Returns:
            A dictionary containing hypermedia pagination information.
        """
        #  "Index must be a non-negative integer"
        assert isinstance(index, int) and index >= 0
        #  "Page size must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0

        data = []
        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)
        next_index = index + page_size

        # If index is out of range, return an empty data list
        if index >= total_items:
            return {
                "index": index,
                "next_index": None,
                "page_size": page_size,
                "data": data
            }

        # Ensure next_index does not exceed the total number of items
        next_index = min(next_index, total_items)

        # Collect data from indexed dataset
        for i in range(index, next_index):
            if i in indexed_dataset:
                data.append(indexed_dataset[i])

        return {
            "index": index,
            "next_index": next_index if next_index < total_items else None,
            "page_size": page_size,
            "data": data
        }
