import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# 1. Configurar la conexión a PostgreSQL de forma segura con SQLAlchemy

USER = "postgres"
PASSWORD = "12345678"  
HOST = "localhost"
PORT = "5432"
DB_NAME = "industrial_plant_db"

db_url = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
engine = create_engine(db_url)

print("🔌 Conexión establecida con éxito a PostgreSQL.")

# 2. Extraer datos usando consultas analíticas SQL directamente a Pandas
print("\n📊 Extrayendo datos para el análisis...")

# Consulta A: Estado de los lotes químicos actuales
query_lotes = """
SELECT producto_quimico, rendimiento_obtenido, estado_lote 
FROM lotes_produccion;
"""
df_lotes = pd.read_sql(query_lotes, engine)

# Consulta B: Alertas de seguridad por exceso de temperatura (> 100°C)
query_alertas = """
SELECT l.producto_quimico, s.id_lote, s.timestamp_lectura, s.temperatura_celsius, s.presion_psi
FROM sensores_monitoreo s
JOIN lotes_produccion l ON s.id_lote = l.id_lote
WHERE s.temperatura_celsius > 100.0;
"""
df_alertas = pd.read_sql(query_alertas, engine)

# 3. Mostrar un resumen rápido en la terminal
print("\n--- RESUMEN DE LOTES ENCONTRADOS ---")
print(df_lotes)

print("\n--- 🚨 ALERTAS DE SEGURIDAD DETECTADAS ---")
if df_alertas.empty:
    print("Todo bajo control. No hay anomalías térmicas críticas.")
else:
    print(df_alertas)

# 4. Generar visualización automatizada
print("\n📈 Generando gráficos del reporte industrial...")
sns.set_theme(style="whitegrid")

# Crear una figura con espacio para dos gráficos
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1: Rendimiento por tipo de Producto Químico
sns.barplot(
    data=df_lotes, 
    x="producto_quimico", 
    y="rendimiento_obtenido", 
    hue="estado_lote",
    ax=axes[0],
    palette="Set2"
)
axes[0].set_title("Eficiencia de Producción por Compuesto (Yield %)")
axes[0].set_ylabel("Rendimiento (%)")
axes[0].set_xlabel("Producto Químico")

# Gráfico 2: Monitoreo de picos de Presión vs Temperatura en situaciones críticas
if not df_alertas.empty:
    sns.scatterplot(
        data=df_alertas,
        x="temperatura_celsius",
        y="presion_psi",
        hue="producto_quimico",
        s=150,
        ax=axes[1],
        color="red"
    )
    axes[1].set_title("Puntos Críticos: Presión vs Temperatura (>100°C)")
    axes[1].set_xlabel("Temperatura (°C)")
    axes[1].set_ylabel("Presión (PSI)")
else:
    axes[1].text(0.5, 0.5, "Sin alertas registradas", ha='center', va='center')
    axes[1].set_title("Monitoreo de Alertas Críticas")

# Ajustar diseño y guardar la imagen para el portafolio de GitHub
plt.tight_layout()
plt.savefig("reporte_monitoreo_planta.png", dpi=300)
print("💾 Gráfico guardado con éxito como 'reporte_monitoreo_planta.png'.")

# Mostrar el gráfico en pantalla
plt.show()