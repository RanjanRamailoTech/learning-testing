import pytest
import scripts.shapes as shapes

# with class based we can use a single instanceto test but in function based tests we need to create multiple instances.
#instead use fixtures
"""
 Fixtures help in preparing test environments, such as creating test data, 
 connecting to a database, initializing objects, etc., before the actual test runs. 
 They also ensure cleanup after the test completes.
"""

# @pytest.fixture
# def my_rectangle():
#     return shapes.Rectangle(10, 20)


# @pytest.fixture
# def other_rectangle():
#     return shapes.Rectangle(5,6)
#these fixtures are transferred to conftest.py    

def test_area(my_rectangle):
    # rectangle = shapes.Rectangle(10, 20)
    assert my_rectangle.area() == 10*20
    

def test_perimeter(my_rectangle):
    # rectangle = shapes.Rectangle(10, 20)
    assert my_rectangle.perimeter() == 2*(10+20)
    
def test_not_equal(my_rectangle, other_rectangle):
    assert my_rectangle != other_rectangle
    
    
"""
SCOPE OF Fixtures:

@pytest.fixture(scope="class")

scope can be function, class, module, session, package

Session fixure is also called as global fixure.
Global fixtures can also be defined in a designated file "conftest.py" 

"""