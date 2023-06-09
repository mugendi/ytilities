"""
 Copyright (c) 2023 Anthony Mugendi
 
 This software is released under the MIT License.
 https://opensource.org/licenses/MIT
"""

from ytilities.paths import path_truncate


def test_truncate():
    path = "/home/mugz/.cache/mozilla/firefox/glbiq5w9.default-release\
        /safebrowsing/allow-flashallow-digest256.sbstore"
    truncated = path_truncate(path)

    assert truncated == "/home/mugz/.cache/.../allow-flashallow-digest256.sbstore"

    truncated = path_truncate(path, 30)

    assert truncated == ".../allow-flashallow-digest256.sbstore"
