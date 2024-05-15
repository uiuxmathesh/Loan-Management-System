from .ILoanRepository import ILoanRepository

class ILoanRepositoryImpl(ILoanRepository):

    def applyLoan(self, Loan):
        query = """INSERT INTO [Loan] (
                                    [LoanID], [CustomerID], 
                                    [principal_amount], [interest_rate], 
                                    [loan_term], [loan_type], 
                                    [loan_status]
                                    ) 
                                    VALUES (?, ?, ?, ?, ?, ?, ?)""" 
        values = (
                Loan.loanID, Loan.customerID, 
                Loan.principal_amount, Loan.interest_rate, 
                Loan.term, Loan.type, 
                'Pending'
                )
        self.cursor.execute(query, values)

    def calculateInterest(self, LoanId:int) -> float:
        try:
            result = self.getLoanbyId(LoanId)
        except Exception as e:
            print(e)
            return
        else:
            principal_amount = result[2]
            interest_rate = result[3]
            tenure = result[4]
            interest = (principal_amount * interest_rate * tenure) / 12
            return interest

    def loanStatus(self, LoanId:int) -> str:
        query = """ SELECT [CustomerID] FROM [Loan] WHERE [LoanID] = ?"""
        self.cursor.execute(query, (LoanId,))
        customerID = self.cursor.fetchone()[0]
        query = """ SELECT [Credit_score] FROM [Customer] WHERE [CustomerID] = ?"""
        self.cursor.execute(query, (customerID,))
        credit_score = self.cursor.fetchone()[0]
        if credit_score > 650:
            status = 'Approved'
        else:
            status = 'Rejected'
        query = """ UPDATE [Loan] SET [loan_status] = ? WHERE [LoanID] = ?"""
        self.cursor.execute(query, (status, LoanId))
        return status

    def calculateEMI(self, LoanId:int) -> float:
        result = self.getLoanbyId(LoanId)
        principal_amount = result[2]
        monthy_interest = (result[3] / 12) / 100
        loan_term = result[4]
        emi = (principal_amount * monthy_interest * (1 + monthy_interest) ** loan_term) / ((1 + monthy_interest) ** loan_term - 1)
        return emi
        

    def loanRepayment(self, LoanId:int, amount:float) -> float:
        monthly_emi = self.calculateEMI(LoanId)
        if amount < monthly_emi:
            print("Payment Rejected. Insufficient payment.")
            return
        else:
            pass

    def getAllLoans(self) -> list:
        query = """ SELECT * FROM [Loan]"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def getLoanbyId(self, LoanId:int):
        query = """ SELECT * FROM [Loan] WHERE [LoanID] = ?"""
        self.cursor.execute(query, (LoanId,))
        result = self.cursor.fetchone()
        if len(result) == 0:
            pass # handle error
        else:
            return result