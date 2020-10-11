import unittest # Importing the unittest module
import pyperclip
from passwords import Passwords

class TestPasswords(unittest.TestCase):

    def setUp(self):
        '''
        The Set up method is to run before each test case.
        '''
        self.new_Password = Passwords("JohnDoe","johndoe2020")

    def tearDown(self):
        '''
        Using tearDown method ensures after every testrun there is a clean up.
        tearDown method ensures accurate results.
        '''
    
