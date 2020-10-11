import unittest # Importing the unittest module
import pyperclip
from passwords import Passwords

class TestPasswords(unittest.TestCase):

    def setUp(self):
        '''
        The Set up method is to run before each test case.
        '''
        self.new_Passwords = Passwords("JohnDoe","johndoe2020")

    def tearDown(self):
        '''
        Using tearDown method ensures after every testrun there is a clean up.
        tearDown method ensures accurate results.
        '''
    
    def test_init(self):
        '''
        The first test case is to confirm the objects is instatiated correctly.
        '''
        self.assertEqual(self.new_Passwords.login_name,"JohnDoe")
        self.assertEqual(self.new_Passwords.password,"johndoe2020")


if __name__ == '__main__':
    unittest.main()
