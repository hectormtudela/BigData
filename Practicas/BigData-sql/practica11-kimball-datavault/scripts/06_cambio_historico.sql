INSERT INTO dbo.Sat_Cliente
    (HubClienteKey, FechaCarga, ClienteNombre, RecordSource)
SELECT HubClienteKey, '2026-10-14T10:00:00', N'Ana G. García', 'TIENDA'
FROM dbo.Hub_Cliente
WHERE ClienteID = 'C01';

SELECT h.ClienteID, s.ClienteNombre, s.FechaCarga
FROM dbo.Hub_Cliente AS h
JOIN dbo.Sat_Cliente AS s ON h.HubClienteKey = s.HubClienteKey
WHERE h.ClienteID = 'C01'
ORDER BY s.FechaCarga;