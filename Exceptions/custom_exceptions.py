class InvalidLoanException(Exception):
    def __init__(self, loanId):
        super().__init__(f"Custom_Exception Raised: Invalid Loan: Loan with ID {loanId} does not exist")