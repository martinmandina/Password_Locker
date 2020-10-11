import pyperclip

class credentials:
    """
    Class that generates new instances of credentialss.
    """

    credentials_list = [] # Empty credentials list

    def __init__(self,account,login_name,password):

      

        self.account = account
        self.login_name = login_name
        self.password = password