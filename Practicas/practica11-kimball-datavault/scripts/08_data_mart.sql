CREATE VIEW dbo.Vista_Mart_Ventas AS
WITH ProductoActual AS (
    SELECT h.HubProductoKey,
           s.ProductoNombre,
           ROW_NUMBER() OVER (
               PARTITION BY h.HubProductoKey
               ORDER BY s.FechaCarga DESC
           ) AS rn
    FROM dbo.Hub_Producto AS h
    JOIN dbo.Sat_Producto AS s ON s.HubProductoKey = h.HubProductoKey
),
VentaActual AS (
    SELECT LinkVentaKey, FechaVenta, Cantidad,
           ROW_NUMBER() OVER (
               PARTITION BY LinkVentaKey
               ORDER BY FechaCarga DESC
           ) AS rn
    FROM dbo.Sat_Venta
)
SELECT l.VentaID,
       v.FechaVenta,
       c.ClienteNombre,
       p.ProductoNombre,
       v.Cantidad
FROM dbo.Link_Venta AS l
JOIN dbo.Hub_Cliente AS hc ON hc.HubClienteKey = l.HubClienteKey
JOIN dbo.BV_ClienteActual AS c ON c.ClienteID = hc.ClienteID
JOIN ProductoActual AS p ON p.HubProductoKey = l.HubProductoKey AND p.rn = 1
JOIN VentaActual AS v ON v.LinkVentaKey = l.LinkVentaKey AND v.rn = 1;
GO

SELECT * FROM dbo.Vista_Mart_Ventas ORDER BY VentaID;


SELECT ProductoNombre,
       SUM(Cantidad) AS UnidadesVendidas
FROM dbo.Vista_Mart_Ventas
GROUP BY ProductoNombre
ORDER BY UnidadesVendidas DESC;