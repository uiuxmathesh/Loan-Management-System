
class Loan:
    
    def __init__(self):
        self._loanID = None
        self._customerID = None
        self._principal_amount = None
        self._term = None
        self._status = None
        self._type = None

    @property
    def loanID(self):
        return self._loanID
    
    @loanID.setter
    def loanID(self, loanID):
        if not isinstance(loanID, int):
            print("Loan ID must be an Number.")
            return
        else:
            self._loanID = loanID

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
    def principal_amount(self):
        return self._principal_amount
    
    @principal_amount.setter
    def principal_amount(self, amount):
        if not isinstance(amount, int):
            print("Amount must be an Number.")
            return
        else:
            self._principal_amount = amount

    @property
    def term(self):
        return self._term
    
    @term.setter
    def term(self, term):
        if not isinstance(term, int):
            print("Term must be an Number.")
            return
        else:
            self._term = term

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        if len(status) == 0:
            print("Status cannot be empty.")
            return
        self._status = status

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if len(type) == 0:
            print("Type cannot be empty.")
            return
        self._type = type