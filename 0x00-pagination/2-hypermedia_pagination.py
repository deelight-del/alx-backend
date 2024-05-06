#!/usr/bin/env python3

"""In this module, we define a helper function
that takes two integer arguments, page and page_size and then take
a step further by implementing a Server clasee to do some stuff."""


from typing import Tuple, List, Dict, Any
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function that returns the start and end index that
    corresponds to the range of indexes to return"""
    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
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
        """Function to get page from the start idx to end idx"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_idx, end_idx = index_range(page, page_size)
        try:
            return self.dataset()[start_idx:end_idx]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """The equivalent of get page, but gets the hypermedia instead"""
        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": (
                    None if (page_size * page) > len(self.dataset())
                    else page + 1
            ),
            "prev_page": (
                None if page <= 0
                else page - 1
            ),
            "total_pages": math.ceil(len(self.dataset()) / page_size)
        }
