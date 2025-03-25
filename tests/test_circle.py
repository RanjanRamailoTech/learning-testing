import pytest
import math
import scripts.shapes as shapes

class TestCircle:
    
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)
	
    def teardown_method(self, method):
        print(f"tearing down  {method}")
        del self.circle
        
    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius **2
        
    def test_perimeter(self):
        result = self.circle.perimeter()
        
        assert result == 2* math.pi * self.circle.radius
        
    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()


#setup method
"""
	The setup method is defined to run setup code before each test method. 
 SO for all the test methods or test classes or functions that we write inside 
 our class based tests, the setup method wil run at the be beginning of each test.
"""

#Teardown method
"""
run tear-down ciode after each test method. 
"""