import pyperclip

class Credentials:
    '''
    This class will generate new instances of credentials
    '''

    credentials_list = []
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

    def save_credentials(self):

        '''
        save_credential method saves credential objects into passwords_list
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes credentials from out list.
        '''

        Credentials.credentials_list.remove(self)
    