"""
In pytest, @pytest.mark is used to categorize, filter, and customize tests. Markers help in running specific subsets of tests instead of executing the entire test suite.
"""

###### Built-in Markers in Pytest

import pytest
import sys

#Skip a test unconditionally.
@pytest.mark.skip
def test_skipped():
    assert 1 == 1  # This test won't run


#Skip with a Condition
@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+") #Skips the test if Python version is below 3.8.
def test_skip_condition():
    assert 2 + 2 == 4

#Mark a Test as Expected to Fail (@pytest.mark.xfail)

@pytest.mark.xfail
def test_expected_fail():
    assert 1 == 2  # This test will fail, but won’t fail the test run


#XFail with a Condition
@pytest.mark.xfail(reason="Known bug in version 1.0")
def test_known_bug():
    assert 1 == 2  # Expected to fail


#  Running Tests in Parallel (@pytest.mark.parametrize) - Run the same test multiple times with different inputs.
@pytest.mark.parametrize("num, expected", [(2, 4), (3, 9), (4, 16)])
def test_square(num, expected):
    assert num ** 2 == expected

#Runs the test 3 times, each with a different (num, expected) pair.


#Custom Order of Test Execution (@pytest.mark.order)
#can specify test execution order.
@pytest.mark.order(2)
def test_second():
    assert 2 == 2

@pytest.mark.order(1)
def test_first():
    assert 1 == 1


#NOTE
"""
We can run a specific tests based on the marker. Say we want to run the test_skip_condition (skipif marker). We can explicitly mention it during the test execution as:

pytest -m skipif  #This will run the tests that are marked skipif
pytest -m "not slow" # this will run ever tests that are not marked slow i.e skip the test marked as slow

pytest --markers # list available markers
"""



#CUSTOM MARKERS
#You must register custom markers in pytest.ini before using them. 
# 
# Create a pytest.ini file and add 
"""
[pytest]
markers =
    smoke: Quick tests to check basic functionality
    regression: Full system tests to check for regressions
    slow: Tests that take longer to run

"""


#Using custom markers
@pytest.mark.smoke
def test_login():
    assert "user" in "user123"

@pytest.mark.regression
def test_full_registration():
    assert 10 + 10 == 20

@pytest.mark.slow
def test_data_processing():
    assert sum(range(10000)) > 0
