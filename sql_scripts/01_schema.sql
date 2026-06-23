-- 1. Crear tabla de Reactores
CREATE TABLE reactores (
    id_reactor SERIAL PRIMARY KEY,
    nombre_reactor VARCHAR(50) NOT NULL,
    capacidad_litros NUMERIC(10, 2),
    estado_actual VARCHAR(20) DEFAULT 'Activo', -- Activo, Mantenimiento, Parada de Emergencia
    fecha_instalacion DATE
);

-- 2. Crear tabla de Lotes de Producción
CREATE TABLE lotes_produccion (
    id_lote SERIAL PRIMARY KEY,
    id_reactor INT REFERENCES reactores(id_reactor) ON DELETE CASCADE,
    producto_quimico VARCHAR(100) NOT NULL,
    fecha_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_fin TIMESTAMP,
    rendimiento_obtenido NUMERIC(5, 2), -- Porcentaje de éxito del lote (Yield)
    estado_lote VARCHAR(20) DEFAULT 'En Proceso' -- En Proceso, Aprobado, Rechazado
);

-- 3. Crear tabla de Monitoreo de Sensores (Datos de Series Temporales)
CREATE TABLE sensores_monitoreo (
    id_lectura BIGSERIAL PRIMARY KEY,
    id_lote INT REFERENCES lotes_produccion(id_lote) ON DELETE CASCADE,
    timestamp_lectura TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperatura_celsius NUMERIC(5, 2) NOT NULL,
    presion_psi NUMERIC(5, 2) NOT NULL,
    nivel_ph NUMERIC(4, 2) NOT NULL
);