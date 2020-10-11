import unittest # Importing the unittest module
import pyperclip
from passwords import Passwords

class TestPasswords(unittest.TestCase):

    def setUp(self):
        '''
        The Set up method is to run before each test case.
        '''
        self.new_passwords = Passwords("JohnDoe","johndoe2020")

    def tearDown(self):
        '''
        Using tearDown method ensures after every testrun there is a clean up.
        tearDown method ensures accurate results.
        '''
        Passwords.passwords_list = []
  
    def test_init(self):
        '''
        The first test case is to confirm the objects is instatiated correctly.
        '''
        self.assertEqual(self.new_passwords.login_name,"JohnDoe")
        self.assertEqual(self.new_passwords.password,"johndoe2020")


if __name__ == '__main__':
    unittest.main()
