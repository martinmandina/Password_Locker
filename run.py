#!/usr/bin/env python3.6

from passwords import Passwords
from credentials import Credentials

def create_passwords(login_name,password):
    '''
    This is a function that creates a new password
    '''
    new_passwords = Passwords(login_name,password)
    return new_passwords
    


