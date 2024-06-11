import requests
import json
import os
from datetime import datetime

API_SECRET_KEY = 'API_KEY'
START_RULE_ID = 1
END_IPS_RULE_ID = 10250

base_url = 'https://workload.us-1.cloudone.trendmicro.com/api/intrusionpreventionrules/'

headers = {
    'api-secret-key': API_SECRET_KEY,
    'api-version': 'v1',
    'accept': 'application/json'
}

# Abrir el archivo para escribir una vez fuera del bucle
current_datetime = datetime.now().strftime("%Y%m%d")
json_filename = f"ipsrules_{current_datetime}.json"
csv_filename = f"ipsrules_{current_datetime}.csv"

with open(json_filename, "w") as file:
    while START_RULE_ID <= END_IPS_RULE_ID:
        url = f"{base_url}{START_RULE_ID}"
        response = requests.get(url, headers=headers)

        if response.status_code == 404 or response.json().get("message") == "Not Found":
            print(f"No data found at ID {START_RULE_ID}.")
        else:
            plugin_info = response.json()
            #print(json.dumps(plugin_info, indent=2))

            # Guardar el resultado en el mismo archivo JSON
            json.dump(plugin_info, file, indent=2)
            file.write("\n")

        START_RULE_ID += 1

# Construir el comando para procesar el archivo JSON con jq y guardar los datos en un archivo CSV
cat_command = (
    f'echo "ID,Name,Severity,DetectMode,Type,Depends,CVE" > {csv_filename} && '
    f'cat {json_filename} | jq -r \'' +
    '{ID: .ID, name: .name, Severity: .severity, detectMode: .detectOnly, Type: .type, ' +
    'Depends: (.dependsOnRuleIDs // [] | join("|")), CVE: (.CVE // [] | join("|"))} ' +
    '| [.ID, .name, .Severity, .detectMode, .Type, .Depends, .CVE] | @csv\' >> ' +
    f'{csv_filename}'
)

# Ejecutar el comando
os.system(cat_command)
print(f'CSV file created: {csv_filename}')
