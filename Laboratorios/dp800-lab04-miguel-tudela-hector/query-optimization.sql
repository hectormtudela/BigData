-- =============================================
-- File: query-optimization.sql
-- Purpose: Compare original query against Copilot's optimization suggestions
-- Author: Héctor Miguel Tudela
-- =============================================

-- ORIGINAL QUERY (before optimization)
SELECT *
FROM SalesLT.SalesOrderHeader h, SalesLT.SalesOrderDetail d, SalesLT.Product p
WHERE h.SalesOrderID = d.SalesOrderID
AND d.ProductID = p.ProductID
AND h.OrderDate > '2008-01-01';


/*
COPILOT'S SUGGESTED OPTIMIZATIONS:
1. Replace comma-style joins with ANSI JOIN syntax (INNER JOIN ... ON ...)
2. Avoid SELECT * -- list only the columns actually needed
3. Use consistent table aliases
4. Add supporting indexes on OrderDate, SalesOrderID and ProductID
5. Rewrite the date filter as a range (>= ... AND < ...)

REVIEW NOTE:
Point 5 as suggested by Copilot changes the meaning of the query, not just its
style: '>= 2008-01-01 AND < 2009-01-01' returns ONLY orders from 2008, while
the original '> 2008-01-01' returns every order from that date onward, with
no upper bound. The corrected version below keeps Copilot's style
improvements but preserves the original filtering logic.
*/

-- OPTIMIZED QUERY (style improvements applied, original date logic preserved)
SELECT
    h.SalesOrderID,
    h.OrderDate,
    d.SalesOrderDetailID,
    d.ProductID,
    d.OrderQty,
    d.UnitPrice,
    p.Name AS ProductName,
    p.Color,
    p.StandardCost
FROM SalesLT.SalesOrderHeader AS h
INNER JOIN SalesLT.SalesOrderDetail AS d
    ON h.SalesOrderID = d.SalesOrderID
INNER JOIN SalesLT.Product AS p
    ON d.ProductID = p.ProductID
WHERE h.OrderDate > '2008-01-01';


-- Suggested supporting indexes (review before creating; not required to run the queries above)
-- CREATE INDEX IX_SalesOrderHeader_OrderDate ON SalesLT.SalesOrderHeader (OrderDate);
-- CREATE INDEX IX_SalesOrderDetail_SalesOrderID ON SalesLT.SalesOrderDetail (SalesOrderID);
-- CREATE INDEX IX_SalesOrderDetail_ProductID ON SalesLT.SalesOrderDetail (ProductID);


-- VERIFICATION: confirm both queries return the same number of rows
SELECT COUNT(*) AS FilasOriginal
FROM SalesLT.SalesOrderHeader h, SalesLT.SalesOrderDetail d, SalesLT.Product p
WHERE h.SalesOrderID = d.SalesOrderID
AND d.ProductID = p.ProductID
AND h.OrderDate > '2008-01-01';

SELECT COUNT(*) AS FilasOptimizada
FROM SalesLT.SalesOrderHeader AS h
INNER JOIN SalesLT.SalesOrderDetail AS d
    ON h.SalesOrderID = d.SalesOrderID
INNER JOIN SalesLT.Product AS p
    ON d.ProductID = p.ProductID
WHERE h.OrderDate > '2008-01-01';