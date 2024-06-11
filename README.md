# Trend Micro Cloud One Intrusion Prevention Rules Fetcher

Este script en Python obtiene reglas de prevención de intrusiones (IPS) desde la API de Trend Micro Cloud One y guarda los datos en archivos JSON y CSV.

## Requisitos

- La La herramienta `jq` instalada en tu sistema
- Claves de API TrendMicro

## Instalación

1. Clonar este repositorio.
   ```sh
   git clone https://github.com/k0jir0900/deepsecurity_ipsrules.git
   cd deepsecurity_ipsrules
    ```
2. Instalación `JQ`:
   En Debian/Ubuntu:
      ```bash
      sudo apt-get install jq
      ```
## Uso
1. Define las claves de la API de Tenable en el script:
    ```python
    API_SECRET_KEY = 'tu_access_key'
    ```

2. Ejecuta el script:
    ```bash
    python3 ipsrules_download.py
    ```

3. Se generarán dos archivos con nombre `ipsrules_YYYYMMDD.json` y `ipsrules_YYYYMMDD.csv`, donde `YYYYMMDD` es la fecha actual.

## Estructura del archivo

El archivo CSV generado contiene las siguientes columnas:

- ID: El ID de la regla.
- Name: El nombre de la regla.
- Severity: La severidad de la regla.
- DetectMode: El modo de detección (si solo detecta).
- Type: El tipo de regla.
- Depends: Las reglas de las que depende.
- CVE: Las identificaciones CVE asociadas.

## Notas

- Asegúrate de que las claves de la API sean correctas y tengan los permisos necesarios.
- La ejecución del script dura aproximadamente 2 Horas.
- Puedes modificar las variables (`START_RULE_ID`) y (`END_RULE_ID`) para modificar el rango de reglas que desees descargar.
