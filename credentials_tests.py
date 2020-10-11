import unittest
import pyperclip
from credentials import Credentials
  
class TestPasswords(unittest.TestCase):

    def setUp(self):
        '''
        The set up method defines instructions that will be run,
        before each test method.
        '''
    
        self.new_Credentials = Credentials("gmail","JohnDoe","johndoe2020")

    def tearDown(self):
        '''
        TearDown method executes a set of instructions,
        this to ensure accurate results
        '''

        Credentials.Credentials_list = []

