/*
  View: SalesLT.vw_ProductSalesAnalysis
  Purpose: Summarizes product sales activity for AdventureWorksLT
  Author: Hector Miguel Tudela
*/
CREATE OR ALTER VIEW SalesLT.vw_ProductSalesAnalysis
AS
SELECT
    p.ProductID,
    p.Name AS ProductName,
    pc.Name AS CategoryName,
    SUM(d.OrderQty) AS TotalQuantitySold,
    SUM(d.LineTotal) AS TotalRevenue,
    AVG(d.UnitPrice) AS AverageSalePrice,
    COUNT(DISTINCT d.SalesOrderID) AS NumberOfOrders
FROM SalesLT.Product AS p
INNER JOIN SalesLT.ProductCategory AS pc
    ON p.ProductCategoryID = pc.ProductCategoryID
INNER JOIN SalesLT.SalesOrderDetail AS d
    ON p.ProductID = d.ProductID
GROUP BY
    p.ProductID,
    p.Name,
    pc.Name;
GO
