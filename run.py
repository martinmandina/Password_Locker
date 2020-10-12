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


    def find_passwords(login_name):
        '''
        This function matches a password by login_name and returns the passsword.
        '''
        return passwords.find_by_login_name(login_name)


    def check_existing_passwords(login_name):
        '''
        This function checks if a password exists with the above login_name and returns a boolean.
        '''
        return passwords.passwords_exist(login_name)


    def display_passwords():
        '''
        This function checks and returns all the saved passwords
        '''
        return passwords.display_passwords()


    # def copy_login_name(passwords)
    #     '''
    #     This Function copies a login_name
    #     '''
    
    def main():
        print("Hello user Welcome to your passwords list. What is your name?")
        user_name = input()

        print("Hello {user_name}. what would you like to do?")
        print('\n')

if __name__== '__main__':
        main()         




