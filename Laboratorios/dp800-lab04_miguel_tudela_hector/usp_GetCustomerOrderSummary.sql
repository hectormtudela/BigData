/*
  Procedure: dbo.usp_GetCustomerOrderSummary
  Purpose: Returns customer order summary data from AdventureWorksLT
  Author: Héctor Miguel Tudela
*/
CREATE OR ALTER PROCEDURE dbo.usp_GetCustomerOrderSummary
    @CustomerID INT = NULL
AS
BEGIN
    SET NOCOUNT ON;

    BEGIN TRY
        SELECT
            c.CustomerID,
            c.FirstName + ' ' + c.LastName AS CustomerName,
            COUNT(DISTINCT h.SalesOrderID) AS TotalOrders,
            COALESCE(SUM(d.LineTotal), 0) AS TotalOrderAmount,
            MAX(h.OrderDate) AS LastOrderDate
        FROM SalesLT.Customer AS c
        LEFT JOIN SalesLT.SalesOrderHeader AS h
            ON c.CustomerID = h.CustomerID
        LEFT JOIN SalesLT.SalesOrderDetail AS d
            ON h.SalesOrderID = d.SalesOrderID
        WHERE @CustomerID IS NULL
            OR c.CustomerID = @CustomerID
        GROUP BY
            c.CustomerID,
            c.FirstName,
            c.LastName
        ORDER BY
            c.CustomerID;
    END TRY
    BEGIN CATCH
        THROW;
    END CATCH
END;
GO