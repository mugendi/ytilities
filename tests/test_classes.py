"""
 Copyright (c) 2023 Anthony Mugendi
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
"""

from ytilities.classes import get_props, is_class, is_initialized


class TestClass:
    def__prop = True

    def __init__(self, val) -> None:
        self.init_prop = val

    def method_1(self):
        print("method")


test_class = TestClass(20)


def test_is_class():
    assert is_class(TestClass)


def test_not_class():
    vars = [1, "a", [1], {"a"}, {"a": 1}, (1, "a"), 1.002, None, True]
    for var in vars:
        assert not is_class(var)


def test_is_initialized():
    assert is_initialized(test_class)


def test_is_not_initialized():
    assert not is_initialized(TestClass)


def test_class_props_uninitialized():
    props = get_props(TestClass)
    assert props == {"def__prop", "method_1"}


def test_class_props_initialized():
    props = get_props(test_class)
    assert props == {"method_1", "def__prop", "init_prop"}


def test_class_props_callable():
    props = get_props(TestClass, filter_callable=True)
    assert props == {"method_1"}


def test_class_props_initialized_with_meta():
    props = get_props(test_class, with_meta=True)
    assert props["def__prop"] == {"type": "bool", "value": True}
