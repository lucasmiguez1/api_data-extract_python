import requests

#URL de la API
url = "https://datausa.io/api/data"

#Parámetros de la API para obtener los datos
params = {
    "drilldowns": "Nation",
    "measures": "Population"
}

#Llamada a la API para obtener los datos de población
response = requests.get(url, params=params)

#Check de si la llamada fue exitosa
if response.status_code == 200:
    #Convertir la respuesta JSON en un diccionario
    data = response.json()
else:
    # Si hubo un error en la solicitud, mostrar mensaje y establecer data como None
    print("Error en la solicitud:", response.status_code)
    data = None

#Diccionario para almacenar la información de población por nación y la información de la fuente
data_dict = {}

#Si se obtuvieron datos de la API, procesar la información
if data:
    #Iterar a través de los datos de la respuesta
    for item in data["data"]:
        #Extraer campos relevantes para cada nación
        nation_id = item["ID Nation"]
        year = item["Year"]
        population = item["Population"]
        nation_name = item["Nation"]
        slug_nation = item["Slug Nation"]

        #Si aún no existe una entrada para la nación, crear un nuevo diccionario para almacenar sus datos
        if nation_id not in data_dict:
            data_dict[nation_id] = {
                "Nation": nation_name,
                "Slug Nation": slug_nation,
                "Population Data": []
            }

        #Agregar los datos de población para cada año al diccionario correspondiente
        data_dict[nation_id]["Population Data"].append({
            "Year": year,
            "Population": population
        })

    #Incluir información adicional de la fuente si está presente en los datos de la respuesta
    if "source" in data:
        source_info = data["source"][0]
        source_annotations = source_info["annotations"]

        #Agregar información de la fuente al diccionario
        data_dict["Source Info"] = {
            "Measures": source_info["measures"],
            "Source Name": source_annotations["source_name"],
            "Source Description": source_annotations["source_description"],
            "Dataset Name": source_annotations["dataset_name"],
            "Dataset Link": source_annotations["dataset_link"],
            "Table ID": source_annotations["table_id"],
            "Topic": source_annotations["topic"]
        }

#Imprimir el diccionario resultante que contiene la información de población por nación y la información de la fuente
print(data_dict)
