SELECT 'Hub_Cliente' AS Tabla, COUNT(*) AS Filas FROM dbo.Hub_Cliente
UNION ALL SELECT 'Hub_Producto', COUNT(*) FROM dbo.Hub_Producto
UNION ALL SELECT 'Sat_Cliente',  COUNT(*) FROM dbo.Sat_Cliente
UNION ALL SELECT 'Sat_Producto', COUNT(*) FROM dbo.Sat_Producto
UNION ALL SELECT 'Link_Venta',   COUNT(*) FROM dbo.Link_Venta
UNION ALL SELECT 'Sat_Venta',    COUNT(*) FROM dbo.Sat_Venta;