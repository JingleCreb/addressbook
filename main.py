#
# Classes
#

class Person(object):
    '''A person I might want to contact.'''
    
    def __init__(self):
        self.title = None
        self.forenames = None
        self.surname = None
        self.addresses = None
        self.emails = None
        self.telephones = None
    
    def output_dict(self):
        '''Returns a dictionary containing the object data (for JSON).'''
        output = {
            'title':        self.title,
            'forenames':    self.forenames,
            'surname':      self.surname,
            'addresses':    [address.output_dict() for address in self.addresses],
            'emails':       [email.output_dict() for email in self.emails],
            'telephones':   [telephone.output_dict() for telephone in self.telephones]
            }
        return output
    
    def input_dict(self, person_dict):
        '''Updates the object with data from a dictionary.'''
        self.title = person_dict['title']
        self.forenames = person_dict['forenames']
        self.surname = person_dict['surname']
        self.addresses = person_dict['addresses']
        self.emails = person_dict['emails']
        self.telephones = person_dict['telephones']

class Address(object):
    '''A geographical address.'''
    
    def __init__(self):
        self.street_address = None
        self.locality = None
        self.city = None
        self.region = None
        self.postcode = None
        self.country = None
        self.live = None
        self.address_type = None
    
    def output_dict(self):
        '''Returns a dictionary containing the object data (for JSON).'''
        output = {
            'street_address':   self.street_address,
            'locality':         self.locality,
            'city':             self.city,
            'region':           self.region,
            'postcode':         self.postcode,
            'country':          self.country,
            'live':             str(self.live),
            'address_type':     self.address_type
            }
    
    def input_dict(self, address_dict):
        '''Updates the object with data from a dictionary.'''
        self.street_address = address_dict['street_address']
        self.locality = address_dict['locality']
        self.city = address_dict['city']
        self.region = address_dict['region']
        self.postcode = address_dict['postcode']
        self.country = address_dict['country']
        if address_dict['live'] == 'True':
            self.live = True
        else:
            self.live = False
        self.address_type = address_dict['address_type']

class Email(object):
    '''An email address.'''
    
    def __init__(self):
        self.email_address = None
        self.live = None
        self.email_type = None
    
    def output_dict(self):
        '''Returns a dictionary containing the object data (for JSON).'''
        output = {
            'email_address':    self.email_address,
            'live':             str(self.live),
            'email_type':       self.email_type
            }
        return output
    
    def input_dict(self, email_dict):
        '''Updates the object with data from a dictionary.'''
        self.email_address = email_dict['email_address']
        if email_dict['live'] == 'True':
            self.live = True
        else:
            self.live = False
        self.email_type = email_dict['email_type']

class Telephone(object):
    '''A telephone number.'''
    
    def __init__(self):
        self.number = None
        self.live = None
        self.number_type = None

    def output_dict(self):
        '''Returns a dictionary containing the object data (for JSON).'''
        output = {
            'number':       self.number,
            'live':         str(self.live),
            'number_type':  self.number_type
        }
        return output
    
    def input_dict(self, telephone_dict):
        '''Updates the object with data from a dictionary.'''
        self.number = telephone_dict['number']
        if telephone_dict['live'] = 'True':
            self.live = True
        else:
            self.live = False
        self.number_type = telephone_dict['number_type']

#
# Basic functions
#

def new_person():
    '''Manual input of a new person.'''
    input_data = {}
    input_data['title'] = input('Title: ')
    input_data['forenames'] = input('Forenames: ')
    input_data['surname'] = input('Surname: ')
    input_data['addresses'] = new_addresses()
    input_data['emails'] = new_emails()
    input_data['telephones'] = new_telephones()
    
    person = Person()
    person.input_dict(input_data)
    
    return 

def new_addresses():
    '''Manual input of a series of addresses.'''
    addresses = []
    answer = input('Enter an address? ')
    while answer.toupper in ('YES', 'Y'):
        addresses.append(new_address())
        answer = input('Enter an address? ')
    
    return addresses
    
def new_address():
    '''Manual input of an address.'''
    address_dict = {
        'street_address':   input('Street address: '),
        'locality':         input('Locality: '),
        'city':             input('City: '),
        'region':           input('Region: '),
        'postcode':         input('Postcode: '),
        'country':          input('Country: '),
        'address_type':     input('Address type: ')
        }
    
    is_live = '':
    while is_live.toupper() not in ('YES', 'Y', 'NO', 'N'):
        is_live = input('Live: ')
    if is_live in ('YES', 'Y'):
        address_dict['live'] = 'True'
    else:
        address_dict['live'] = 'False'
    
    address = Address()
    address.input_dict(address_dict)
    
    return address

def new_emails():
    pass

def new_telephones():
    pass
