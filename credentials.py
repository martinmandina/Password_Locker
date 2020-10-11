import pyperclip

class Credentials:
    '''
    This class will generate new instances of credentials
    '''

    Credentials_list = []
    '''
    Created empty Credentials list
    '''

    def __init__(self,account,login_name,password):

        self.account = account
        self.login_name = login_name
        self.password = password

    '''
    Create constructur and pass 4 arguments.
    The self argument above is a special keyword.
    '''