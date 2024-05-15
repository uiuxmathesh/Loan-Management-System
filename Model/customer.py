
class Customer:

    def __init__(self):
        self._customerID = None
        self._name = None
        self._email = None
        self._phone = None
        self._address = None
        self._credit_score = None

    @property
    def customerID(self):
        return self._customerID
    
    @customerID.setter
    def customerID(self, customerID):
        if not isinstance(customerID, int):
            print("Customer ID must be an Number.")
            return
        else:
            self._customerID = customerID

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if len(name) == 0:
            print("Name cannot be empty.")
            return
        self._name = name

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if len(email) == 0:
            print("Email cannot be empty.")
            return
        self._email = email

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        if len(phone) != 10:
            print("Phone number must be 10 digits long.")
            return
        self._phone = phone

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        if len(address) == 0:
            print("Address cannot be empty.")
            return
        self._address = address
    
    @property
    def credit_score(self):
        return self._credit_score
    
    @credit_score.setter
    def credit_score(self, credit_score):
        if not isinstance(credit_score, float):
            print("Credit score must be an Number.")
            return
        self._credit_score = credit_score

    def __str__(self):
        return f"Customer ID: {self.customerID}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}, Credit Score: {self.credit_score}"

    