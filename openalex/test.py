"""
Tests to ensure pacakge is working.
"""
from .works import Works
TITLE = "Examples of Effective Data Sharing in Scientific Publishing"

def test_bibt():
    """
    Tests to check working function in package.
    """
    res = Works("https://doi.org/10.1021/acscatal.5b00538")
    assert TITLE == res.new()
