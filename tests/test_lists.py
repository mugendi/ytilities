"""
 Copyright (c) 2023 Anthony Mugendi
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
"""

import numpy as np

from ytilities.lists import chunk_arr, flatten, listify


def test_listify():
    v = "a"
    assert listify(v) == ["a"]
    v = ["a", "b"]
    assert listify(v) == ["a", "b"]


def test_flatten_numpy_array():
    arr = np.random.rand(3, 8)
    assert arr.shape == (3, 8)
    flat = flatten(arr)
    assert flat.shape == (24,)


def test_flatten_list():
    arr = [1, 2, 3, [4, 5, 6, [7, 8, 9, [10]]]]
    flat = flatten(arr)
    assert flat == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_flatten_tuple():
    arr = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    flat = flatten(arr)
    assert flat == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def test_flatten_set():
    arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    flat = flatten(arr)
    assert flat == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


def test_chunk_arr():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    chunks = chunk_arr(arr, 2)

    assert len(chunks) == 5 and chunks[3] == [7, 8]
