#!/usr/bin/env python3.6

from passwords import Passwords
from credentials import Credentials

    def create_passwords(login_name,password):
        '''
        This is a function that creates a new password
        '''
        new_passwords = Passwords(login_name,password)
        return new_passwords


    def save_passwords(passwords):
        '''
        A save_passwords function that takes in a password object.
        '''
         password.save_passwords()


    def del_passwords(passwords):
        '''
        This function del_passwords deletes a contact
        '''
        passwords.delete_passwords()




# if __name__== '__main__':
#         main()         




