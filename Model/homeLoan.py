from .loan import Loan

class HomeLoan(Loan):

    _interest_rate = 0.095

    @property
    def property_address(self):
        return self._property_address
    
    @property_address.setter
    def property_address(self, address):
        if len(address) == 0:
            print("Address cannot be empty.")
            return
        self._property_address = address

    @property   
    def property_value(self):
        return self._property_value
    
    @property_value.setter
    def property_value(self, value):
        if not isinstance(value, int):
            print("Value must be an Number.")
            return
        else:
            self._property_value = value
