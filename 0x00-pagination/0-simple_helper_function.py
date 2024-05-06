#!/usr/bin/env python3

"""In this module, we define a helper function
that takes two integer arguments, page and page_size"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns the start and end index that
    corresponds to the range of indexes to return"""
    return (page_size * (page - 1), page_size * page)
