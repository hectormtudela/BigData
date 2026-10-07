 -- Mask SSN to show only last 4 digits
 ALTER TABLE dbo.Employees
 ALTER COLUMN SSN ADD MASKED WITH (FUNCTION = 'partial(0, "XXX-XX-", 4)');

 -- Mask Salary with a random value
 ALTER TABLE dbo.Employees
 ALTER COLUMN Salary ADD MASKED WITH (FUNCTION = 'random(50000, 150000)');

 -- Mask Email to show first character and domain
 ALTER TABLE dbo.Employees
 ALTER COLUMN Email ADD MASKED WITH (FUNCTION = 'email()');