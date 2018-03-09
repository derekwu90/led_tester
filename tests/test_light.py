#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from lights.main import creategrid
from lights.lightgrid import LightGrid
from lights.parsefile import parsefile

__author__ = "derekwu90"
__copyright__ = "derekwu90"
__license__ = "mit"


def test_data():
    localfile="/home/wu/comp30670/assignment3/lights/data/test_data.txt"
    with pytest.raises(AssertionError, message="Excepting an error, there is no error here"):
        N,instructions=parsefile(localfile)
        print(creategrid(N,instructions).count())
        
def test_data1():
    localfile="/home/wu/comp30670/assignment3/lights/data/test_data1.txt"
    with pytest.raises(AssertionError, message="Excepting an error, there is no error here"):
        N,instructions=parsefile(localfile)
        print(creategrid(N,instructions).count())

def test_data2():
    localfile="/home/wu/comp30670/assignment3/lights/data/test_data2.txt"
    with pytest.raises(AssertionError, message="Excepting an error, there is no error here"):
        N,instructions=parsefile(localfile)
        print(creategrid(N,instructions).count())   
        
def test_data3():
    localfile="/home/wu/comp30670/assignment3/lights/data/test_data3.txt"
    with pytest.raises(AssertionError, message="Excepting an error, there is no error here"):
        N,instructions=parsefile(localfile)
        print(creategrid(N,instructions).count())   