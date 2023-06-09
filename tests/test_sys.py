"""
 Copyright (c) 2023 Anthony Mugendi
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
"""

from ytilities.system import trace_caller


def func():
    return trace_caller(True)


def test_pick():
    # class
    s = func()

    assert "test_pick" in s[1]


if __name__ == "__main__":
    test_pick()
