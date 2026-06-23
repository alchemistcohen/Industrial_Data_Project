-- CONSULTA 1: Resumen de eficiencia por producto químico (Métricas Clave)
SELECT 
    producto_quimico,
    COUNT(id_lote) AS total_lotes,
    ROUND(AVG(rendimiento_obtenido), 2) AS rendimiento_promedio,
    SUM(CASE WHEN estado_lote = 'Rechazado' THEN 1 ELSE 0 END) AS lotes_rechazados
FROM lotes_produccion
GROUP BY producto_quimico;

-- CONSULTA 2: Reporte de picos críticos de presión y temperatura
-- Muestra el valor máximo registrado por cada lote que superó los límites de seguridad
SELECT 
    l.id_lote,
    l.producto_quimico,
    MAX(s.temperatura_celsius) AS max_temperatura_registrada,
    MAX(s.presion_psi) AS max_presion_registrada,
    COUNT(s.id_lectura) AS numero_de_alertas
FROM sensores_monitoreo s
JOIN lotes_produccion l ON s.id_lote = l.id_lote
WHERE s.temperatura_celsius > 100.0 OR s.presion_psi > 60.0
GROUP BY l.id_lote, l.producto_quimico;