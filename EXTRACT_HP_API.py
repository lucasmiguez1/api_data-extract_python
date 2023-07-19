#Librería necesaria para extraer los datos
import requests

#Función para chequear el status de la API y extraer sus datos
def obtener_datos_api(url):
    try:
        #Llamada a la API
        response = requests.get(url)

        #Checkear si la llamada fue exitosa
        if response.status_code == 200:
            datos = response.json()
            return datos
        else:
            print("Error al obtener los datos de la API. Código de estado:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)
        return None

#URL de la API
url_api = "https://hp-api.onrender.com/api/characters/staff"

#Invocación de la función para extraer datos
datos_api = obtener_datos_api(url_api)

#Condicional para chequear que se extrayeron los datos
if datos_api:
        print(f"Datos obtenidos: {datos_api}")

        #Obtener los campos ordenados en una lista
        campos_ordenados = list(datos_api[0].keys())

        print(f"Campos ordenados: {campos_ordenados}")
else:
        print("No se pudieron obtener los datos de la API")
