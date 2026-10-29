DROP TABLE IF EXISTS dbo.Sat_Cliente
CREATE TABLE dbo.Sat_Cliente (
    HubClienteKey INT NOT NULL,
    FechaCarga    DATETIME2(0) NOT NULL,
    ClienteNombre NVARCHAR(100) NOT NULL,
    RecordSource  VARCHAR(30) NOT NULL,
    CONSTRAINT PK_Sat_Cliente PRIMARY KEY (HubClienteKey, FechaCarga),
    CONSTRAINT FK_Sat_Cliente_Hub FOREIGN KEY (HubClienteKey)
        REFERENCES dbo.Hub_Cliente(HubClienteKey)
);

DROP TABLE IF EXISTS dbo.Sat_Producto
CREATE TABLE dbo.Sat_Producto (
    HubProductoKey INT NOT NULL,
    FechaCarga     DATETIME2(0) NOT NULL,
    ProductoNombre NVARCHAR(100) NOT NULL,
    RecordSource   VARCHAR(30) NOT NULL,
    CONSTRAINT PK_Sat_Producto PRIMARY KEY (HubProductoKey, FechaCarga),
    CONSTRAINT FK_Sat_Producto_Hub FOREIGN KEY (HubProductoKey)
        REFERENCES dbo.Hub_Producto(HubProductoKey)
);
GO

WITH Clientes AS (
    SELECT ClienteID, ClienteNombre, FechaCarga, RecordSource,
           ROW_NUMBER() OVER (PARTITION BY ClienteID, FechaCarga ORDER BY VentaID) AS rn
    FROM dbo.Stage_Ventas
)
INSERT INTO dbo.Sat_Cliente (HubClienteKey, FechaCarga, ClienteNombre, RecordSource)
SELECT h.HubClienteKey, c.FechaCarga, c.ClienteNombre, c.RecordSource
FROM Clientes AS c
JOIN dbo.Hub_Cliente AS h ON h.ClienteID = c.ClienteID
WHERE c.rn = 1;

WITH Productos AS (
    SELECT ProductoID, ProductoNombre, FechaCarga, RecordSource,
           ROW_NUMBER() OVER (PARTITION BY ProductoID, FechaCarga ORDER BY VentaID) AS rn
    FROM dbo.Stage_Ventas
)
INSERT INTO dbo.Sat_Producto (HubProductoKey, FechaCarga, ProductoNombre, RecordSource)
SELECT h.HubProductoKey, p.FechaCarga, p.ProductoNombre, p.RecordSource
FROM Productos AS p
JOIN dbo.Hub_Producto AS h ON h.ProductoID = p.ProductoID
WHERE p.rn = 1;

SELECT * FROM dbo.Sat_Cliente;
SELECT * FROM dbo.Sat_Producto;