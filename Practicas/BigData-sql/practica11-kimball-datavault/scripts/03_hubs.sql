DROP TABLE IF EXISTS dbo.Hub_Cliente
CREATE TABLE dbo.Hub_Cliente (
    HubClienteKey INT IDENTITY(1,1) PRIMARY KEY,
    ClienteID     VARCHAR(10) NOT NULL UNIQUE,
    FechaCarga    DATETIME2(0) NOT NULL,
    RecordSource  VARCHAR(30) NOT NULL
);

DROP TABLE IF EXISTS dbo.Hub_Producto
CREATE TABLE dbo.Hub_Producto (
    HubProductoKey INT IDENTITY(1,1) PRIMARY KEY,
    ProductoID     VARCHAR(10) NOT NULL UNIQUE,
    FechaCarga     DATETIME2(0) NOT NULL,
    RecordSource   VARCHAR(30) NOT NULL
);
GO


WITH Clientes AS (
    SELECT ClienteID, FechaCarga, RecordSource,
           ROW_NUMBER() OVER (PARTITION BY ClienteID ORDER BY FechaCarga, VentaID) AS rn
    FROM dbo.Stage_Ventas
)
INSERT INTO dbo.Hub_Cliente (ClienteID, FechaCarga, RecordSource)
SELECT ClienteID, FechaCarga, RecordSource FROM Clientes WHERE rn = 1;

WITH Productos AS (
    SELECT ProductoID, FechaCarga, RecordSource,
           ROW_NUMBER() OVER (PARTITION BY ProductoID ORDER BY FechaCarga, VentaID) AS rn
    FROM dbo.Stage_Ventas
)
INSERT INTO dbo.Hub_Producto (ProductoID, FechaCarga, RecordSource)
SELECT ProductoID, FechaCarga, RecordSource FROM Productos WHERE rn = 1;

SELECT * FROM dbo.Hub_Cliente;
SELECT * FROM dbo.Hub_Producto;