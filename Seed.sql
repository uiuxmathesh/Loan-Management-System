INSERT INTO Customer (CustomerID, Name, Email, Phone, Address, Credit_score)
VALUES
    (1, 'John Doe', 'john.doe@example.com', '1234567890', '123 Main St, Anytown, USA', 750),
    (2, 'Jane Smith', 'jane.smith@example.com', '9876543210', '456 Elm St, Somewhere, USA', 800),
    (3, 'Michael Johnson', 'michael.johnson@example.com', '1112223333', '789 Oak St, Nowhere, USA', 700),
    (4, 'Emily Brown', 'emily.brown@example.com', '4445556666', '321 Maple St, Anytown, USA', 720),
    (5, 'David Lee', 'david.lee@example.com', '7778889999', '654 Pine St, Elsewhere, USA', 780);


INSERT INTO Loan (CustomerID, principal_amount, interest_rate, loan_term, loan_type, loan_status)
VALUES
    ( 1, 20000, 5.5, 36, 'CarLoan', 'Pending'),
    ( 2, 300000, 4.25, 360, 'HomeLoan', 'Approved'),
    ( 3, 15000, 6.0, 24, 'CarLoan', 'Approved'),
    ( 4, 250000, 3.75, 240, 'HomeLoan', 'Approved'),
    ( 5, 10000, 7.0, 12, 'CarLoan', 'Pending');

SELECT * FROM [Customer]

SELECT * FROM [Loan]