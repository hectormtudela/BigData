USE DataWarehouse;
GO

EXEC bronze.load_bronze;   -- 1. Fuentes → Bronze
EXEC silver.load_silver;   -- 2. Bronze → Silver

USE msdb;
GO

-- Si el trabajo ya existe, lo eliminamos para poder recrearlo
IF EXISTS (SELECT 1 FROM dbo.sysjobs WHERE name = N'DWH - Carga diaria')
    EXEC dbo.sp_delete_job @job_name = N'DWH - Carga diaria';
GO

-- 1. El trabajo
EXEC dbo.sp_add_job
    @job_name    = N'DWH - Carga diaria',
    @description = N'Recarga completa de las capas Bronze y Silver del DataWarehouse',
    @enabled     = 1;

-- 2. Paso 1: Bronze. Si termina bien, pasa al siguiente; si falla, el trabajo se detiene con error
EXEC dbo.sp_add_jobstep
    @job_name          = N'DWH - Carga diaria',
    @step_name         = N'1 - Cargar Bronze',
    @subsystem         = N'TSQL',
    @database_name     = N'DataWarehouse',
    @command           = N'EXEC bronze.load_bronze;',
    @on_success_action = 3,    -- 3 = ir al siguiente paso
    @on_fail_action    = 2;    -- 2 = terminar el trabajo con error

-- 3. Paso 2: Silver. Solo se ejecuta si Bronze terminó bien
EXEC dbo.sp_add_jobstep
    @job_name          = N'DWH - Carga diaria',
    @step_name         = N'2 - Cargar Silver',
    @subsystem         = N'TSQL',
    @database_name     = N'DataWarehouse',
    @command           = N'EXEC silver.load_silver;',
    @on_success_action = 1,    -- 1 = terminar el trabajo con éxito
    @on_fail_action    = 2;

-- 4. Programación: todos los días a las 06:00
EXEC dbo.sp_add_schedule
    @schedule_name     = N'Diario 06:00',
    @freq_type         = 4,       -- 4 = diario
    @freq_interval     = 1,       -- cada 1 día
    @active_start_time = 060000;  -- formato HHMMSS

EXEC dbo.sp_attach_schedule
    @job_name      = N'DWH - Carga diaria',
    @schedule_name = N'Diario 06:00';

-- 5. Asignar el trabajo a este servidor
EXEC dbo.sp_add_jobserver
    @job_name    = N'DWH - Carga diaria',
    @server_name = N'(local)';
GO

	BEGIN CATCH
		PRINT '=========================================='
		PRINT 'ERROR OCCURED DURING LOADING BRONZE LAYER'
		PRINT 'Error Message' + ERROR_MESSAGE();
		PRINT 'Error Message' + CAST (ERROR_NUMBER() AS NVARCHAR);
		PRINT 'Error Message' + CAST (ERROR_STATE() AS NVARCHAR);
		PRINT '=========================================='
		THROW;  -- Añadido: relanza el error para que SQL Server Agent detecte el fallo
	END CATCH