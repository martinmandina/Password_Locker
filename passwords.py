import pyperclip

class Passwords:
    '''
    Class that generates new instances of passwords.
    '''
    passwords_list = []
    
    
    def __init__(self,user_name,password):
        
        self.user_name = user_name
        self.password = password
    '''
    Creates Constructur and passed 3 arguments.
    The self argument above is a special keyword.
    '''
    passwords_list = []


    def save_passwords(self):
        '''
        create a save_passwords method that is called on,
        a contact object.
        '''
        Passwords.passwords_list.append(self)


    def delete_passwords(self):
        '''
        delete_passwords method deletes a saved passwords from the passwords_list
        '''

        Passwords.passwords_list.remove(self)


    @classmethod
    def find_password_by_user_name(cls,Passwords):
        '''
        a decorator that belongs to the whole class.

        login   :   login name to search for
        Returns : passwords of person that matches the string user name.
        '''

        for password in cls.passwords_list:
            if Passwords.password == password:
                return password

    @classmethod
    def passwords_exists(cls,string):
        '''
        Method that checks if a password exists from the password list.
        Args:
            string: Password to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''

        for Passwords in cls.passwords_list:
            if Passwords.password == string:
                return True
        return False

    @classmethod
    def display_passwords(cls):
        '''
        method that returns the password and displays them
        '''
        return cls.passwords_list
    





    
        
