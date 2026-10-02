 -- Mask credit card to show only last 4 digits
 ALTER TABLE dbo.Customers
 ALTER COLUMN CreditCardNumber ADD MASKED WITH (FUNCTION = 'partial(0, "XXXX-XXXX-XXXX-", 4)');

 -- Mask phone number to show only last 4 digits
 ALTER TABLE dbo.Customers
 ALTER COLUMN Phone ADD MASKED WITH (FUNCTION = 'partial(0, "XXX-XXX-", 4)');