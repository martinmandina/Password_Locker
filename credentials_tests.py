import unittest
import pyperclip
from credentials import Credentials
  
class TestPasswords(unittest.TestCase):

    def setUp(self):
        '''
        The set up method defines instructions that will be run,
        before each test method.
        '''
    
        self.new_credentials = Credentials("gmail","JohnDoe","johndoe2020")

    def tearDown(self):
        '''
        TearDown method executes a set of instructions,
        this to ensure accurate results
        '''

        Credentials.credentials_list = []

    def test_init(self):
        '''
        Create a test_instance to check if all our objects are instatiated correctly
        '''

        self.assertEqual(self.new_credentials.account,"gmail")
        self.assertEqual(self.new_credentials.login_name,"JohnDoe")
        self.assertEqual(self.new_credentials.password,"johndoe2020")

if __name__ == '__main__':
    unittest.main()        

