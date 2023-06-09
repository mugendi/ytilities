"""
 Copyright (c) 2023 Anthony Mugendi
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
"""

from ytilities.numbers import human_format


def test_format_human():
    nums = {2345: "2.345K", 56: "56.0", 7e8: "700.0M"}

    for num, human_str in nums.items():
        assert human_format(num) == human_str
