class Contact:
    """
    Class that generates new instances of contacts
    """

    pass

contact_list = [] # Empty contact list
# Init method up here
def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)
        
def delete_contact(self):
    
        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self)
            
@classmethod
def find_by_number(cls,number):
            '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

            for contact in cls.contact_list:
                if contact.phone_number == number:
                    return contact
