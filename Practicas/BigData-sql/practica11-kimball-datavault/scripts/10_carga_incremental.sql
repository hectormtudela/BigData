IF NOT EXISTS (SELECT 1 FROM dbo.Stage_Ventas WHERE VentaID = 4)
    INSERT INTO dbo.Stage_Ventas
        (VentaID, ClienteID, ClienteNombre, ProductoID,
         ProductoNombre, FechaVenta, Cantidad, FechaCarga, RecordSource)
    VALUES
        (4, 'C02', N'Luis Pérez', 'P01', N'Teclado',
         '2026-10-03', 5, '2026-10-15T09:00:00', 'TIENDA');
GO

IF OBJECT_ID('tempdb..#Nuevas') IS NOT NULL DROP TABLE #Nuevas;

SELECT s.*
INTO #Nuevas
FROM dbo.Stage_Ventas AS s
WHERE NOT EXISTS (SELECT 1 FROM dbo.Link_Venta AS l WHERE l.VentaID = s.VentaID);

INSERT INTO dbo.Hub_Cliente (ClienteID, FechaCarga, RecordSource)
SELECT n.ClienteID, MIN(n.FechaCarga), MIN(n.RecordSource)
FROM #Nuevas AS n
WHERE NOT EXISTS (SELECT 1 FROM dbo.Hub_Cliente h WHERE h.ClienteID = n.ClienteID)
GROUP BY n.ClienteID;

INSERT INTO dbo.Hub_Producto (ProductoID, FechaCarga, RecordSource)
SELECT n.ProductoID, MIN(n.FechaCarga), MIN(n.RecordSource)
FROM #Nuevas AS n
WHERE NOT EXISTS (SELECT 1 FROM dbo.Hub_Producto h WHERE h.ProductoID = n.ProductoID)
GROUP BY n.ProductoID;

WITH CliNuevos AS (
    SELECT n.ClienteID, n.ClienteNombre, n.FechaCarga, n.RecordSource,
           ROW_NUMBER() OVER (PARTITION BY n.ClienteID
                              ORDER BY n.FechaCarga DESC, n.VentaID DESC) AS rn
    FROM #Nuevas AS n
)
INSERT INTO dbo.Sat_Cliente (HubClienteKey, FechaCarga, ClienteNombre, RecordSource)
SELECT h.HubClienteKey, c.FechaCarga, c.ClienteNombre, c.RecordSource
FROM CliNuevos AS c
JOIN dbo.Hub_Cliente AS h ON h.ClienteID = c.ClienteID
WHERE c.rn = 1
  AND NOT EXISTS (
        SELECT 1 FROM dbo.Sat_Cliente AS s
        WHERE s.HubClienteKey = h.HubClienteKey
          AND s.FechaCarga = (SELECT MAX(s2.FechaCarga) FROM dbo.Sat_Cliente s2
                              WHERE s2.HubClienteKey = h.HubClienteKey)
          AND s.ClienteNombre = c.ClienteNombre)
  AND NOT EXISTS (
        SELECT 1 FROM dbo.Sat_Cliente AS s
        WHERE s.HubClienteKey = h.HubClienteKey AND s.FechaCarga = c.FechaCarga);

WITH ProNuevos AS (
    SELECT n.ProductoID, n.ProductoNombre, n.FechaCarga, n.RecordSource,
           ROW_NUMBER() OVER (PARTITION BY n.ProductoID
                              ORDER BY n.FechaCarga DESC, n.VentaID DESC) AS rn
    FROM #Nuevas AS n
)
INSERT INTO dbo.Sat_Producto (HubProductoKey, FechaCarga, ProductoNombre, RecordSource)
SELECT h.HubProductoKey, p.FechaCarga, p.ProductoNombre, p.RecordSource
FROM ProNuevos AS p
JOIN dbo.Hub_Producto AS h ON h.ProductoID = p.ProductoID
WHERE p.rn = 1
  AND NOT EXISTS (
        SELECT 1 FROM dbo.Sat_Producto AS s
        WHERE s.HubProductoKey = h.HubProductoKey
          AND s.FechaCarga = (SELECT MAX(s2.FechaCarga) FROM dbo.Sat_Producto s2
                              WHERE s2.HubProductoKey = h.HubProductoKey)
          AND s.ProductoNombre = p.ProductoNombre)
  AND NOT EXISTS (
        SELECT 1 FROM dbo.Sat_Producto AS s
        WHERE s.HubProductoKey = h.HubProductoKey AND s.FechaCarga = p.FechaCarga);

        INSERT INTO dbo.Link_Venta
    (VentaID, HubClienteKey, HubProductoKey, FechaCarga, RecordSource)
SELECT n.VentaID, c.HubClienteKey, p.HubProductoKey, n.FechaCarga, n.RecordSource
FROM #Nuevas AS n
JOIN dbo.Hub_Cliente  AS c ON c.ClienteID  = n.ClienteID
JOIN dbo.Hub_Producto AS p ON p.ProductoID = n.ProductoID;

INSERT INTO dbo.Sat_Venta
    (LinkVentaKey, FechaCarga, FechaVenta, Cantidad, RecordSource)
SELECT l.LinkVentaKey, n.FechaCarga, n.FechaVenta, n.Cantidad, n.RecordSource
FROM #Nuevas AS n
JOIN dbo.Link_Venta AS l ON l.VentaID = n.VentaID
WHERE NOT EXISTS (SELECT 1 FROM dbo.Sat_Venta sv
                  WHERE sv.LinkVentaKey = l.LinkVentaKey AND sv.FechaCarga = n.FechaCarga);

DROP TABLE #Nuevas;
GO