from abc import ABC, abstractmethod

class ILoanRepository(ABC):
    @abstractmethod
    def applyLoan(self, Loan):
        pass

    @abstractmethod
    def calculateInterest(self, LoanId:int) -> float:
        pass

    @abstractmethod
    def loanStatus(self, LoanId:int) -> str:
        pass

    @abstractmethod
    def calculateEMI(self, LoanId:int) -> float:
        pass

    @abstractmethod
    def loanRepayment(self, LoanId:int, amount:float) -> float:
        pass

    @abstractmethod
    def getAllLoans(self) -> list:
        pass

    @abstractmethod
    def getLoanbyId(self, LoanId:int):
        pass