DROP TABLE IF EXISTS dbo.Stage_Ventas
CREATE TABLE dbo.Stage_Ventas (
    VentaID        INT NOT NULL PRIMARY KEY,
    ClienteID      VARCHAR(10) NOT NULL,
    ClienteNombre  NVARCHAR(100) NOT NULL,
    ProductoID     VARCHAR(10) NOT NULL,
    ProductoNombre NVARCHAR(100) NOT NULL,
    FechaVenta     DATE NOT NULL,
    Cantidad       INT NOT NULL,
    FechaCarga     DATETIME2(0) NOT NULL,
    RecordSource   VARCHAR(30) NOT NULL
);
GO

INSERT INTO dbo.Stage_Ventas
    (VentaID, ClienteID, ClienteNombre, ProductoID,
     ProductoNombre, FechaVenta, Cantidad, FechaCarga, RecordSource)
VALUES
    (1, 'C01', N'Ana García', 'P01', N'Teclado', '2026-10-01', 2, '2026-10-13T09:00:00', 'TIENDA'),
    (2, 'C02', N'Luis Pérez', 'P02', N'Ratón',   '2026-10-01', 1, '2026-10-13T09:00:00', 'TIENDA'),
    (3, 'C01', N'Ana García', 'P02', N'Ratón',   '2026-10-02', 3, '2026-10-13T09:00:00', 'TIENDA');
GO

SELECT * FROM dbo.Stage_Ventas ORDER BY VentaID;