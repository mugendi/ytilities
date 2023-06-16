"""
 Copyright (c) 2023 Anthony Mugendi
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
"""

from ytilities.system import importing_script, trace_caller


def func():
    return trace_caller(True)


def test_pick():
    # class
    s = func()

    assert "test_pick" in s[1]


def test_importing_script():
    script = importing_script()
    assert script.endswith("/bin/pytest")


if __name__ == "__main__":
    test_pick()
