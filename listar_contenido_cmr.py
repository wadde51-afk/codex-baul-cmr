import os
from datetime import datetime

# 🔧 Cambia esta ruta si tu baúl está en otro sitio
RUTA_RAIZ = "/storage/emulated/0/Documents/CMR_MASTER_VAULT_2070"

TOTAL_ARCHIVOS = 0
TOTAL_CARPETAS = 0
TOTAL_BYTES = 0

salida = []

for raiz, carpetas, archivos in os.walk(RUTA_RAIZ):
    nivel = raiz.replace(RUTA_RAIZ, "").count(os.sep)
    indent = "  " * nivel
    carpeta_nombre = os.path.basename(raiz) or os.path.basename(RUTA_RAIZ)
    salida.append(f"{indent}{carpeta_nombre}/")
    TOTAL_CARPETAS += 1

    for f in archivos:
        ruta_abs = os.path.join(raiz, f)
        try:
            tam = os.path.getsize(ruta_abs)
            mtime = os.path.getmtime(ruta_abs)
            fecha = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            tam = 0
            fecha = "N/A"
        TOTAL_ARCHIVOS += 1
        TOTAL_BYTES += tam
        salida.append(f"{indent}  {f}  |  {tam//1024} KB  |  {fecha}")

# Guardar reporte junto al script
REPORTE = "reporte_cmr.txt"
with open(REPORTE, "w", encoding="utf-8") as fh:
    fh.write(f"INVENTARIO: {RUTA_RAIZ}\n\n")
    fh.write("\n".join(salida))
    fh.write("\n\n")
    fh.write(f"Total carpetas: {TOTAL_CARPETAS}\n")
    fh.write(f"Total archivos: {TOTAL_ARCHIVOS}\n")
    fh.write(f"Tamaño total: {TOTAL_BYTES/1024/1024:.2f} MB\n")

print(f"✅ Reporte generado: {REPORTE}")
print(f"📂 Carpeta raíz: {RUTA_RAIZ}")
print(f"📊 Carpetas: {TOTAL_CARPETAS} | Archivos: {TOTAL_ARCHIVOS} | Total: {TOTAL_BYTES/1024/1024:.2f} MB")

