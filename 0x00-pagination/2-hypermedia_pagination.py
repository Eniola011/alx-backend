#!/usr/bin/env python3
"""

Hyper Media Pagination

"""


import csv
import math
from typing import Dict, List, Tuple


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            Returns a dictionary containing the following key-value pairs:
            >> page_size: the length of the returned dataset page
            >> page: the current page number
            >> data: the dataset page (equivalent to return from previous task)
            >> next_page: number of the next page, None if no next page
            >> prev_page: number of the previous page, None if no previous page
            >> total_pages: the total number of pages in the dataset as an
               integer
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        hypermedia: Dict = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return hypermedia
