# Sistema de Monitoreo de Procesos y Analítica Industrial IoT ⚙️📊

Este proyecto simula un entorno industrial real para una planta química, integrando una base de datos relacional (**PostgreSQL**) para la gestión operativa y un pipeline de análisis en **Python** para la detección automatizada de anomalías y evaluación de eficiencia (Yield Analytics).

## 🚀 Arquitectura y Flujo de Trabajo
1. **Modelado de Datos (SQL):** Diseño de bases de datos con restricciones de integridad referencial para Reactores, Lotes de Producción y Lecturas de Sensores en series temporales.
2. **Simulación de Datos (Python & NumPy):** Generación estadística de +400 lecturas simuladas de sensores (temperatura, presión, pH) incluyendo la inserción controlada de picos críticos y fallas operativas.
3. **Pipeline Analítico (Pandas & SQLAlchemy):** Extracción automatizada mediante queries relacionales complejas y procesamiento de datos.
4. **Visualización Avanzada (Seaborn & Matplotlib):** Generación automática de reportes visuales de las alertas de seguridad y rendimientos.

## 📈 Insights Destacados del Análisis
* **Detección de Riesgos:** El sistema aisló con éxito **13 alertas críticas de seguridad** en el lote del *Catalizador Nitrado*, registrando temperaturas máximas peligrosas de hasta 115.67°C correlacionadas con incrementos de presión superiores a 70 PSI.
* **Control de Calidad:** Se identificó una desviación crítica en la producción de *Ácido Sulfúrico Diluido*, registrando un rendimiento (*Yield*) de apenas 45%, clasificando el lote como **Rechazado**.

## 🛠️ Tecnologías Utilizadas
* **Base de Datos:** PostgreSQL
* **Lenguaje:** Python 3.12+
* **Librerías Principales:** Pandas, NumPy, SQLAlchemy, Matplotlib, Seaborn
* **Entorno:** Visual Studio Code & pgAdmin 4

## 📂 Estructura del Repositorio
* `/sql_scripts/01_schema.sql`: Creación de tablas, llaves primarias y foráneas.
* `/sql_scripts/02_queries.sql`: Consultas analíticas y KPIs de rendimiento.
* `generar_datos.py`: Script de automatización y simulación de sensores.
* `analisis_planta.py`: Pipeline de extracción de datos y generación del reporte gráfico.