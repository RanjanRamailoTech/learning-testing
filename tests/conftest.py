import pytest
import scripts.shapes as shapes

##These are global fixtures

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)


@pytest.fixture
def other_rectangle():
    return shapes.Rectangle(5,6)