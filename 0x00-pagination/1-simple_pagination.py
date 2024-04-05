#!/usr/bin/env python3
"""

Simple Helper Function

"""


import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Args:
            page: current page.
            page_size: total size of page.
        Return:
            A tuple of size two containing a start index and an end index..
            corresponding to the range of indexes to return in a list..
            for those particular pagination parameters.
    """
    end_index: int = page * page_size
    start_index: int = end_index - page_size

    return (start_index, end_index)


class Server:
    """
        Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Get page and list of pagination
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        range_index: Tuple = index_range(page, page_size)
        pagination: List = self.dataset()

        return (pagination[range_index[0]:range_index[1]])
