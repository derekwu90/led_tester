#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from lights.parsefile import parsefile

__author__ = "derekwu90"
__copyright__ = "derekwu90"
__license__ = "mit"


def test_fib():
    localfile="/home/wu/comp30670/assignment3/lights/data/test_data.txt"
    assert parsefile(localfile) == (10,[['turn on', (0, 0), (9, 9)], ['turn off', (0, 0), (9, 9)], ['switch', (0, 0), (9, 9)], ['turn off', (0, 0), (9, 9)], ['turn on', (2, 2), (7, 7)]])
    with pytest.raises(AssertionError, message="Excepting an error, there is no error here"):
        parsefile(localfile)