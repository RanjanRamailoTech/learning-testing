"""
Mocking is useful when testing functions that depend on external services, databases, APIs, or expensive computations. 
It allows you to replace real objects with fake ones (mocks) to isolate and test specific logic.
A mock is a fake object that replaces a real one, allowing you to: 
✅ Simulate behavior of dependencies
✅ Control return values
✅ Track function calls (e.g., how many times a function was called)

Python provides the unittest.mock module for mocking.
"""


import pytest
from scripts.service import get_user_data, send_email
from unittest.mock import patch, Mock, ANY
import unittest


class TestUserData(unittest.TestCase):
    
    # The behind the patch is that when you pass this string inside the patch decorator, 
    # every occurance or every call of request will be mocked
    @patch('requests.get')
    def test_get_user_data(self, mock_get):
        mock_response = Mock()
        response_dict = {'name': 'John', 'email': 'john@email.com'}
        
        mock_response.json.return_value = response_dict
        
        mock_get.return_value = mock_response
        
        user_data = get_user_data(1)
        #testing the url being called when the mock user data is being called
        
        mock_get.assert_called_with("https://api.example.com/users/1")
        
        assert user_data == response_dict
        
        # Here we just asserted that the user data in the given format is being called whenever the api with id 1 is hit.
        #Note that there was no actual api hit to fetch the data but we mocked the data .
        
        
#lets mock and test the email functionality we defined in service.py file

class TestEmail(unittest.TestCase):
    
    @patch('smtplib.SMTP')
    #when smtplib.SMTP is called we mock the server = smtplib.SMTP(smtp_server, smtp_port) constructor
    def test_send_mail(self, mock_smtp):
        instance = mock_smtp.return_value
        
        send_email("smtp.example.com", 587, "mymail@example.com", "tomail@example.com", "Subject", "Main Content")
        
        mock_smtp.assert_called_with("smtp.example.com", 587)
        #asserting that the correct server with the correct port is being called
        
        instance.starttls.assert_called_with()
        #check is the tls has been called
        
        instance.login.assert_called_with("mymail@example.com", "dummyPassword")
        #check is the login has been called with correct credentials
        
        instance.sendmail.assert_called_with("mymail@example.com", "tomail@example.com", ANY)
        #check is the sendmail has been called with correct data
        
        instance.quit.assert_called_with()
        
        
        