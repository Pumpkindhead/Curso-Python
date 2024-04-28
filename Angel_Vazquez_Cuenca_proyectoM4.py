## Comenzamos importando las bibliotecas necesarias para las funcionaes que utilizaremos en este proyecto ##

import requests
import os
import json

def get_pokemon_data(pokemon_name): #Definimos la función que obtendra los datos del pokemon introducido en la PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200: 
        data = response.json()
        return data
    else:
        return None

def save_pokemon_data_to_json(data, pokemon_name): #Se define la función que se utilizará para guardar los datos de los pokemon buscados en la carpeta pokedex en formato JSON
    folder_path = "pokedex"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, f"{pokemon_name.lower()}.json")
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def display_pokemon_info(data): #Se define la función que mostrará la información del pokemon incluyendo la imagen el peso,altura, habilidades y el tipo del pokemon
    print("Nombre del Pokemon:", data["name"].capitalize())
    print("Peso:", str(data["weight"]) + ' kg')
    print("Altura:", data["height"])
    print("Habilidades:")
    for ability in data["abilities"]:
        print("-", ability["ability"]["name"].capitalize())
    print("Tipo:")
    for type_info in data["types"]:
        print("-", type_info["type"]["name"].capitalize())

    # Obteniendo la URL 
    front_sprite_url = data["sprites"]["front_default"]
    print("Front Image URL:", front_sprite_url)

    # Descargando la imagen
    image_response = requests.get(front_sprite_url)
    image_name = f"{data['name']}.png"
    with open(image_name, "wb") as image_file:
        image_file.write(image_response.content)
    print("Image downloaded successfully!")

def main(): #Finamente esta función solicita al usuario que introduzca el nombre de un pokemon, en caso de encontrarlo muestra la información y en caso que no se encuentre manda un mensaje de que no se encuentra el pokemon
    pokemon_name = input("Introduce el nombre de un Pokemon: ")
    pokemon_data = get_pokemon_data(pokemon_name)
    if pokemon_data:
        display_pokemon_info(pokemon_data) #Se descarga la imagen para guardarla en la carpeta establecida 
        save_pokemon_data_to_json(pokemon_data, pokemon_name)
    else:
        print("Pokemon no encontrado.")

if __name__ == "__main__":
    main()