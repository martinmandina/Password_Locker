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


    def test_save_passwords(self):
        '''
        this test case is to ensure that we can save a password object into out
        passwords list
        '''
        
        self.new_passwords.save_passwords()
        self.assertEqual(len(Passwords.passwords_list),1)


    def test_save_multiple_passwords(self):
        '''
        test_save_multiple_passwords testcase to check if we can save multiple passwords
        objects to our passwords_list
        '''
        
        self.new_passwords.save_passwords()
        test_passwords = Passwords("MartinMandina","martinmandina2020")
        test_passwords.save_passwords()

        self.assertEqual(len(Passwords.passwords_list),2)


    def test_delete_passwords(self):
        '''
        In this testcase we check if we can remove a password object once created
        '''
       
        self.new_passwords.save_passwords()
        test_passwords = Passwords("MartinMandina","martinmandina2020")
        test_passwords.save_passwords()
        self.new_passwords.delete_passwords()

        self.assertEqual(len(Passwords.passwords_list),1)


    def test_find_passwords_by_number(self):
        '''
        test to check if we can find a password by phone number and display information
        '''

        self.new_passwords.save_passwords()
        test_passwords = Passwords("JohnDoe","johndoe2020") # new passwords
        test_passwords.save_passwords()
        found_passwords = Passwords.find_by_login_name("JohnDoe")
        
        self.assertEqual(found_passwords.password,test_passwords.password)


    def test_password_exists(self):
        '''
        check if a password exits and if result can return a boolean value.
        '''
        
        self.new_passwords.save_passwords()
        test_passwords = Passwords("JohnDoe","johndoe2020")
        test_passwords.save_passwords()
        password_exists = Passwords.password_exist("JohnDoe")

        self.assertTrue(password_exists)


    def test_diplay_all_passwords(self):
        '''
        This method returns a list of all saved contacts
        '''

        self.assertEqual(Passwords.display_passwords(),Passwords.passwords_list)



if __name__ == '__main__':
    unittest.main()
