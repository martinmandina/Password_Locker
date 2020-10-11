import pyperclip

class Passwords:
    """
    Class that generates new instances of passwords.
    """

    passwords_list = []
    '''
    Created empty  password list
    '''

    def __init__(self,login_name,password):
           
        self.login_name = login_name
        self.password = password
    '''
    Creates Constructur and passed 3 arguments.
    The self argument above is a special keyword.
    '''

 
   