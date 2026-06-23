import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from datetime import datetime, timedelta

# Configuración de conexión 
db_url = "postgresql://postgres:12345678@localhost:5432/industrial_plant_db"
engine = create_engine(db_url)

print("🚀 Generador de datos industriales activo (Versión Corregida)...")

# 1. Definir los lotes que queremos simular
lotes = [
    {"id_lote": 1, "horas": 12},
    {"id_lote": 2, "horas": 8},
    {"id_lote": 3, "horas": 16}
]

registros = []
base_time = datetime.now() - timedelta(days=2)

# 2. Generar la lista de diccionarios de forma limpia
for lote in lotes:
    id_lote = lote["id_lote"]
    total_lecturas = lote["horas"] * 12  # 12 lecturas por hora (cada 5 min)
    
    for i in range(total_lecturas):
        timestamp = base_time + timedelta(minutes=i * 5)
        
        # Valores base normales
        temp = float(np.random.normal(75, 4))
        presion = float(np.random.normal(45, 2))
        ph = float(np.random.normal(6.5, 0.1))
        
        # Introducir anomalía crítica intencional en el lote 3
        if id_lote == 3 and i > (total_lecturas - 20):
            temp += float(np.random.uniform(25, 40))
            presion += float(np.random.uniform(15, 25))
            
        # El diccionario DEBE tener exactamente las llaves con los nombres de las columnas en SQL
        registros.append({
            "id_lote": int(id_lote),
            "timestamp_lectura": timestamp,
            "temperatura_celsius": float(round(temp, 2)),
            "presion_psi": float(round(presion, 2)),
            "nivel_ph": float(round(ph, 2))
        })

# 3. Convertir a DataFrame de Pandas
df_sensores = pd.DataFrame(registros)

# Forzar explícitamente los tipos de datos para evitar conflictos con SQLAlchemy
df_sensores["id_lote"] = df_sensores["id_lote"].astype(int)
df_sensores["temperatura_celsius"] = df_sensores["temperatura_celsius"].astype(float)
df_sensores["presion_psi"] = df_sensores["presion_psi"].astype(float)
df_sensores["nivel_ph"] = df_sensores["nivel_ph"].astype(float)

# 4. Inserción masiva en PostgreSQL
# 4. Inserción masiva en PostgreSQL
try:
    df_sensores.to_sql("sensores_monitoreo", engine, if_exists="append", index=False)
    print(f"✅ ¡Éxito! Se han insertado {len(df_sensores)} registros limpios en 'sensores_monitoreo'.")
except Exception as e:
    print("❌ Ocurrió un error al insertar en la base de datos.")
    # Forzamos a que el mensaje de error se lea con la codificación de Windows para poder entenderlo
    error_msg = str(e).encode('utf-8', errors='replace').decode('cp1252', errors='replace')
    print(f"Detalle del error descifrado:\n{error_msg}")