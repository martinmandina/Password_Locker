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

def display_passwords():
    '''
    This function checks and returns all the saved passwords
    '''
    return Passwords.display_passwords()



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




    
def main():
    print("Hello user! Welcome, to your password list,\n" 
            "What is your name?\n")
    user_name = input()
    print("-"*30)
    print(f"Hallo {user_name} Welcome.")
    print("-"*30)

    while True:
        print(f"{user_name} Please use these short codes for easier access :\n"
            "cp - to create a new password,\n"
            "dp - display the password,\n"
            "fp - find a password,\n"
            "ex - to exit the passwords list \n")
        print("-"*30)
        short_code = input().lower()
       
        if short_code == 'cp':
            print("-"*30)
            print("Type your username?")
            user_name = input()

            print("-"*30)        
            print("Type your new password")
            password = input()
            print("-"*30)

            save_passwords(create_passwords(user_name,password))
                
            print ('\n')
            print (f'New password {password} created for {user_name}')
            print ('\n')
            print("-"*30)
            
        elif short_code == 'dp':
            print ('\n')
            if display_passwords():
                print("Here is a list of all your passwords")
                print('\n')

                for passwords in display_passwords():
                    #print(f'{account:40s} ({ratio:3.2f}) -> AUD {splitAmount}')
                    print(f'{Passwords.first_name} {Passwords.last_name} {Passwords.phone_number}')
                    print("\n")
            else:
                    print('\n')
                    print(f"{user_name} you dont have any passwords saved at the moment")
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




