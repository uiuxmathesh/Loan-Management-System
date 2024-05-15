from .loan import Loan

class CarLoan(Loan):

    _interest_rate = 0.085

    @property
    def carModel(self):
        return self._carModel
    
    @carModel.setter
    def carModel(self, model):
        if len(model) == 0:
            print("Please Specify Car Model.")
            return
        self._carModel = model

    @property
    def carValue(self):
        return self._carValue
    
    @carValue.setter
    def carValue(self, value):
        if not isinstance(value, int):
            print("Value must be an Number.")
            return
        self._carValue = value

    @property
    def interest_rate(self):
        return self._interest_rate
    
    def __str__(self):
        return f"Customer ID: {self.customerID}, Car Model: {self.carModel}, Car Value: {self.carValue}, Interest Rate: {self.interest_rate}, Loan Amount: {self.principal_amount}, Loan Term: {self.term}"