import pandas as pd
import requests


def download_and_convert_data(url):
    # Download the data from the provided link
    response = requests.get(url)
    data = response.json()

    # Convert the data into a structured format
    structured_data = []
    for pokemon in data['pokemon']:
        pokemon_data = {
            'Name': pokemon['name'],
            'Type': ', '.join(pokemon['type']),
            'Height': pokemon['height'],
            'Weight': pokemon['weight']
        }
        structured_data.append(pokemon_data)

    # Create a DataFrame from the structured data
    df = pd.DataFrame(structured_data)

    # Save the DataFrame as an Excel file
    df.to_excel('pokemon_data.xlsx', index=False)
    print("Data saved as 'pokemon_data.xlsx'.")


# Provide the URL to download the data from
# json link is not working
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

download_and_convert_data(url)
