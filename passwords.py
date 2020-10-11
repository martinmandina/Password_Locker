import pyperclip

class Passwords:
        '''
        Class that generates new instances of passwords.
        '''
        passwords_list = []
        
     
        def __init__(self,login_name,password):
           
            self.login_name = login_name
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
        def find_by_login_name(cls,password):
            '''
            a decorator that belongs to the whole class.
            '''
            for passwords in cls.passwords_list:
                if passwords.login_name == password:
                    return passwords