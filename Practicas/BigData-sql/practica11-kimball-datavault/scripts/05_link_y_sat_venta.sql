CREATE TABLE dbo.Link_Venta (
    LinkVentaKey   INT IDENTITY(1,1) PRIMARY KEY,
    VentaID        INT NOT NULL UNIQUE,
    HubClienteKey  INT NOT NULL,
    HubProductoKey INT NOT NULL,
    FechaCarga     DATETIME2(0) NOT NULL,
    RecordSource   VARCHAR(30) NOT NULL,
    CONSTRAINT FK_Link_Cliente FOREIGN KEY (HubClienteKey)
        REFERENCES dbo.Hub_Cliente(HubClienteKey),
    CONSTRAINT FK_Link_Producto FOREIGN KEY (HubProductoKey)
        REFERENCES dbo.Hub_Producto(HubProductoKey)
);

CREATE TABLE dbo.Sat_Venta (
    LinkVentaKey INT NOT NULL,
    FechaCarga   DATETIME2(0) NOT NULL,
    FechaVenta   DATE NOT NULL,
    Cantidad     INT NOT NULL,
    RecordSource VARCHAR(30) NOT NULL,
    CONSTRAINT PK_Sat_Venta PRIMARY KEY (LinkVentaKey, FechaCarga),
    CONSTRAINT FK_Sat_Venta_Link FOREIGN KEY (LinkVentaKey)
        REFERENCES dbo.Link_Venta(LinkVentaKey),
    CONSTRAINT CK_Sat_Venta_Cantidad CHECK (Cantidad > 0)
);
GO

INSERT INTO dbo.Link_Venta
    (VentaID, HubClienteKey, HubProductoKey, FechaCarga, RecordSource)
SELECT s.VentaID, c.HubClienteKey, p.HubProductoKey, s.FechaCarga, s.RecordSource
FROM dbo.Stage_Ventas AS s
JOIN dbo.Hub_Cliente AS c ON s.ClienteID = c.ClienteID
JOIN dbo.Hub_Producto AS p ON s.ProductoID = p.ProductoID;

INSERT INTO dbo.Sat_Venta
    (LinkVentaKey, FechaCarga, FechaVenta, Cantidad, RecordSource)
SELECT l.LinkVentaKey, s.FechaCarga, s.FechaVenta, s.Cantidad, s.RecordSource
FROM dbo.Stage_Ventas AS s
JOIN dbo.Link_Venta AS l ON s.VentaID = l.VentaID;
GO

SELECT * FROM dbo.Link_Venta;
SELECT * FROM dbo.Sat_Venta;