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

def check_existing_passwords(user_name):
    '''
    This function checks if a password exists with the above login_name and returns a boolean.
    '''
    return Passwords.passwords_exists(user_name)

def find_passwords(user_name):
    '''
    This function matches a password by user
    _name and returns the passsword.
    '''
    return Passwords.find_password_by_user_name(user_name)

def del_passwords(passwords):
    '''
    This function del_passwords deletes a contact
    '''
    passwords.delete_passwords()

   
def main():
    print("Hello user! Welcome, to your password list,\n" 
            "What is your name?\n")
    user_name = input()
    print("-"*30)
    print(f"Hallo {user_name} Welcome.")
    print("-"*30)

    while True:
        print(f"{user_name} Please use these short codes for easier access :\n"
            "cp - to create a new password.\n"
            "dp - display your password or multiple passwords.\n"
            "fp - find your saved password.\n"
            "ex - to exit your passwords list.\n")
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
                print(f"{user_name} this is a list all your passwords you saved")
                print('\n')

                for Passwords in display_passwords():
                    print(f'"{Passwords.password}" ')
                    print("\n")
                    print("-"*30)
            else:
                    print('\n')
                    print(f"{user_name} currently you dont have any passwords saved at the moment")
                    print('\n')

        elif short_code == 'fp':

                print("Enter the 'user name' you used to save your password ")
                print("-"*30)
                user_name = input()
                if check_existing_passwords(user_name):
                        user_name =  find_passwords(user_name)
                        print(f"{user_name.password}")
                        print('-' * 20)

                        print(f"password is ..{user_name.find_password_by_user_name}")
                        print("-"*30)
                else:
                        print("no passwords found that match your 'user name'")
                        print("-"*30)
        elif short_code == "ex":
                print("Thank you....")
                break
        else:
                print("I really didn't get that. Please use the short codes")

if __name__== '__main__':
        main()         




