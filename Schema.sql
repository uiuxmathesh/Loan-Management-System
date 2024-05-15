IF NOT EXISTS(SELECT * FROM sys.databases WHERE [name]='LoanManager')
	BEGIN
		CREATE DATABASE [LoanManager]
	END
	GO
USE	[LoanManager]
GO

IF OBJECT_ID(N'Customer') IS NULL
CREATE TABLE [Customer](
	[CustomerID] int NOT NULL,
	[Name] varchar(255),
	[Email] varchar(255),
	[Phone] varchar(10),
	[Address] varchar(255),
	[Credit_score] float,
	CONSTRAINT Customer_pk PRIMARY KEY ([CustomerID])
);


IF OBJECT_ID(N'Loan') IS NULL
CREATE TABLE [Loan](
	[LoanID] int NOT NULL IDENTITY(100,1),
	[CustomerID] int,
	[principal_amount] float,
	[interest_rate] float,
	[loan_term] int,
	[loan_type] varchar(255) NOT NULL CHECK ([loan_type]IN ('CarLoan','HomeLoan')),
	[loan_status] varchar(255) NOT NULL CHECK ([loan_status]IN ('Pending','Approved')),
	CONSTRAINT loan_pk PRIMARY KEY ([LoanID]),
	CONSTRAINT customer_loan_fk FOREIGN KEY ([CustomerID]) REFERENCES Customer([CustomerID])
);
