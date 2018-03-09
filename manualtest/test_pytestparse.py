import sys
import pytest

from test_parsefun import checkurl, parsefile, ha

def test_ha():
    localfile ="data/test_data.tx"
    N = ha(localfile)
    assert N is not None
    
    
