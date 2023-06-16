"""
 Copyright (c) 2023 Anthony Mugendi
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
"""

from ytilities.misc import pick, unique_eq


class TestClass:
    prop_1 = 1
    prop_2 = 2
    prop_3 = 3
    prop_4 = 4


def test_pick():
    # class
    var = TestClass()
    picked = pick(var, ["prop_1", "prop_2"])
    assert picked == {"prop_1": 1, "prop_2": 2}

    # list
    var = ["a", "b", "c", "d", "e", "f", "g", "h"]
    picked = pick(var, [1, 4, 7])
    assert picked == ["b", "e", "h"]

    # set
    var = {"a", "b", "c", "d", "e", "f", "g", "h"}
    picked = pick(var, ["a", "e", "h"])
    assert picked == {"h", "e", "a"}

    # dict
    var = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
    picked = pick(var, ["a", "e", "h"])
    assert picked == {"a": 1, "e": 5}

    # keys as tuple
    picked = pick(var, ("a", "e", "h"))
    assert picked == {"a": 1, "e": 5}

    # keys as set
    picked = pick(var, {"a", "e", "h"})
    assert picked == {"a": 1, "e": 5}

    # key as str
    picked = pick(var, "c")
    assert picked == {"c": 3}


def test_unique_eq():
    assert unique_eq([1, 2, 5, 3, 4], [1, 2, 3, 4, 5])
    assert unique_eq((1, 2, 5, 3, 4), (1, 2, 3, 4, 5))
    assert unique_eq({1, 2, 5, 3, 4}, {1, 2, 3, 4, 5})
