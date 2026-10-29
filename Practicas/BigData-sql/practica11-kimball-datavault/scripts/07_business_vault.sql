CREATE VIEW dbo.BV_ClienteActual AS
WITH Versiones AS (
    SELECT h.ClienteID,
           s.ClienteNombre,
           s.FechaCarga,
           ROW_NUMBER() OVER (
               PARTITION BY h.ClienteID
               ORDER BY s.FechaCarga DESC
           ) AS rn
    FROM dbo.Hub_Cliente AS h
    JOIN dbo.Sat_Cliente AS s ON s.HubClienteKey = h.HubClienteKey
)
SELECT ClienteID, ClienteNombre, FechaCarga
FROM Versiones
WHERE rn = 1;
GO

SELECT * FROM dbo.BV_ClienteActual ORDER BY ClienteID;