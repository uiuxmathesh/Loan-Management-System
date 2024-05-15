from DAO import ILoanRepositoryImpl
from Model import HomeLoan, CarLoan
from tabulate import tabulate

class Main:
    def __init__(self):
        print("Starting the application......")
        self.loanService = ILoanRepositoryImpl()
        self.optionMenu()

    def optionMenu(self):
        print("*********Welcome to the Loan Management System*******")
        
        while True:
                print("=================Select an option====================")
                print("1. Apply for a loan")
                print("2. Calculate interest")
                print("3. Check loan status")
                print("4. Loan Repayment")
                print("5. Calculate EMI")
                print("6. List all loans")
                print("7. List Loan by ID")
                print("8. Exit")
                print("=====================================================")
                choice = int(input("Please select a option from the menu: "))
                if choice == 1:
                    input_loan_type = input("Enter the type of loan (Home/Car): ")
                    if input_loan_type == "Home":
                        loan = HomeLoan()
                        loan.customerID = int(input("Enter the customer ID: "))
                        loan.property_address = input("Enter the property address: ")
                        loan.property_value = int(input("Enter the property value: "))
                        loan.principal_amount = int(input("Enter the principal amount you need: "))
                        loan.term = int(input("Enter the term of the loan (in months): "))
                        loan.type = "HomeLoan"

                    elif input_loan_type == "Car":
                        loan = CarLoan()
                        loan.customerID = int(input("Enter the customer ID: "))
                        loan.carModel = input("Enter the vehicle model: ")
                        loan.carValue = int(input("Enter the vehicle value: "))
                        loan.principal_amount = int(input("Enter the principal amount you need: "))
                        loan.term = int(input("Enter the term of the loan (in months): "))
                        loan.type = "CarLoan"

                    print(loan.principal_amount)
                    self.loanService.applyLoan(loan)
                
                elif choice == 2:
                    loanID = int(input("Enter the loan ID: "))
                    interest = self.loanService.calculateInterest(loanID)
                    print(f"The interest for the loan is: {interest}")

                elif choice == 3:
                    loanID = int(input("Enter the loan ID: "))
                    status = self.loanService.loanStatus(loanID)
                    print(f"The status of the loan is: {status}")

                elif choice == 4:
                    loanID = int(input("Enter the loan ID: "))
                    amount = int(input("Enter the amount you want to repay: "))
                    self.loanService.loanRepayment(loanID, amount)

                elif choice == 5:
                    loanID = int(input("Enter the loan ID: "))
                    emi = self.loanService.calculateEMI(loanID)
                    print(f"The EMI for the loan is: {emi}")

                elif choice == 6:
                    loans = self.loanService.getAllLoans()
                    print("The list of loans are: ")
                    headers = self.loanService.cursor.description
                    headers = tuple( header[0] for header in headers)
                    headers = [ headers ]
                    result = headers + loans
                    table = tabulate(result, headers='firstrow', tablefmt='fancy_grid')
                    print(table)

                elif choice == 7:
                    loanID = int(input("Enter the loan ID: "))
                    loan = self.loanService.getLoanbyId(loanID)
                    print(f"The loan details are:")
                    headers = self.loanService.cursor.description
                    headers = tuple( header[0] for header in headers)
                    headers = [ headers ]
                    loan = [ loan ]
                    result = headers + loan
                    result = headers + loan
                    table = tabulate(result, headers='firstrow', tablefmt='fancy_grid')
                    print(table)


                elif choice == 8:
                    print("Exiting the application....")
                    self.loanService.connection.close()
                    return

                else:
                    print("Invalid choice. Please select a valid option.")
                    self.optionMenu()



if __name__ == "__main__":

    Main()
        

    
    

