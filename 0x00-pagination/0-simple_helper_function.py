#!/usr/bin/env python3
"""

Simple Helper Function

"""


from typing import Tuple


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
