#!/usr/bin/env python3.6

from passwords import Passwords
from credentials import Credentials

def create_passwords(user_name,password):
    '''
    This is a function that creates a new password
    '''
    new_passwords = Passwords(user_name,password)
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


def find_passwords(user_name):
    '''
    This function matches a password by user
    _name and returns the passsword.
    '''
    return Passwords.find_password_by_user_name(user_name)


def check_existing_passwords(user_name):
    '''
    This function checks if a password exists with the above login_name and returns a boolean.
    '''
    return Passwords.passwords_exists(user_name)


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
        print(f"{user_name} Please use these short codes:\n"
            "cp - to create a new password,\n"
            "dp - display the password,\n"
            "fp - find a password,\n"
            "ex - to exit the passwords list \n")

        short_code = input().lower()

        if short_code == 'cp':
           
            print("-"*15)

            print("user name ....")
            user_name = input()

        
            print("password ...")
            password = input()

            save_passwords(create_passwords(user_name,password))
                
            print ('\n')
            print (f'New password {login_name} {password} created')
            print ('\n')
            print("-"*10)
            
        elif short_code == 'dp':

            if display_passwords():
                print("Here is a list of all your passwords")
                print('\n')

                for passwords in display_passwords():
                    #print(f'{account:40s} ({ratio:3.2f}) -> AUD {splitAmount}')
                    print(f'{Passwords.first_name} {Passwords.last_name} {Passwords.phone_number}')
                    print("\n")
            else:
                    print('\n')
                    print("You dont seem to have any passwordss saved yet")
                    print('\n')

        elif short_code == 'fp':

                print("Enter the login_name you want to search for")

                search_number = input()
                if check_existing_passwords(search_password):
                        search_passwords = find_passwords(login_name)
                        print(f"{search_passwords.login_name} {search_passwords.password}")
                        print('-' * 20)

                        print(f"Phone number.......{search_passwords.phone_number}")
                        print(f"Email address.......{search_passwords.email}")
                else:
                        print("That passwords does not exist")

        elif short_code == "ex":
                print("Bye .......")
                break
        else:
                print("I really didn't get that. Please use the short codes")

if __name__== '__main__':
        main()         




