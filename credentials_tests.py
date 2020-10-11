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


    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the  objects is saved into
        the credentials list
        '''

        self.new_credentials.save_credentials()

        self.assertEqual(len(Credentials.credentials_list),1)


    def test_save_multiple_credentials(self):
        '''
        A test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credentials_list
        '''

        self.new_credentials.save_credentials()
        
        test_credentials = Credentials("twitter","DavidMark","davidmark2020") 
        
        test_credentials.save_credentials()
        
        self.assertEqual(len(Credentials.credentials_list),2) 


    def test_delete_credentials(self):
        '''
        A test_delete_credentials to test if we can remove a credential from our credential list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("twitter","DavidMark","davidmark2020")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials() 
       
        self.assertEqual(len(Credentials.credentials_list),1)


#     def test_find_credentials_by_account(self):
#         '''
#         Test check if we can get credentials by marching account
#         '''
#         self.new_credentials.save_credentials()
#         test_credentials = Credentials("twitter","DavidMark","davidmark2020")
#         test_credentials.save_credentials()

#         found_credentials = Credentials.find_by_account("twitter")


# if __name__ == '__main__':
    unittest.main()        

