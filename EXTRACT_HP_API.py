import requests

def obtener_datos_api(url):
    try:
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            datos = response.json()
            return datos
        else:
            print("Error al obtener los datos de la API. Código de estado:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)
        return None

url_api = "https://hp-api.onrender.com/api/characters/staff"
datos_api = obtener_datos_api(url_api)

if datos_api:
        print("Datos obtenidos:")
        print(datos_api)

        # Obtener los campos ordenados en una lista
        campos_ordenados = list(datos_api[0].keys())

        print("Campos ordenados:")
        print(campos_ordenados)
else:
        print("No se pudieron obtener los datos de la API.")