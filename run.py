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
        passwords.save_passwords()


def del_passwords(passwords):
        '''
        This function del_passwords deletes a contact
        '''
        passwords.delete_passwords()


def find_passwords(login_name):
        '''
        This function matches a password by login_name and returns the passsword.
        '''
        return Passwords.find_by_login_name(login_name)


def check_existing_passwords(login_name):
        '''
        This function checks if a password exists with the above login_name and returns a boolean.
        '''
        return Passwords.passwords_exist(login_name)


def display_passwords():
        '''
        This function checks and returns all the saved passwords
        '''
        return Passwords.display_passwords()


    
def main():
        print("Hello user Welcome to your passwords list. What is your name?")
        user_name = input()

        print(f"Hello {user_name}. what would you like to do?")
        print('\n')

while True:
                    print("Use these short codes : cp - create a new passwords, dp - display passwords, fp -find a passwords, ex -exit the passwords list ")

                    short_code = input().lower()

                    if short_code == 'cp':
                            print("New passwords")
                            print("-"*10)

                            print ("login name ....")
                            login_name = input()

                        
                            print("credential ...")
                            credential = input()

if __name__== '__main__':
        main()         




