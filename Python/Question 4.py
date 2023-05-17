import pandas as pd
import requests


def download_and_convert_data(url):
    # Download the data from the provided link
    response = requests.get(url)
    data = response.json()

    # Convert the data into a structured format
    structured_data = []
    for item in data:
        data_item = {
            'Name': item.get('name', ''),
            'Year': item.get('year', ''),
            'Type': item.get('recclass', ''),
            'Mass (g)': item.get('mass (g)', ''),
            'Fall': item.get('fall', ''),
            'Latitude': item.get('reclat', ''),
            'Longitude': item.get('reclong', '')
        }
        structured_data.append(data_item)

    # Create a DataFrame from the structured data
    df = pd.DataFrame(structured_data)

    # Save the DataFrame as a CSV file
    df.to_csv('meteorite_data.csv', index=False)
    print("Data saved as 'meteorite_data.csv'.")


# Provide the URL to download the data from
url = "https://data.nasa.gov/resource/y77d-th95.json"

# Call the function to download, convert, and save the data
download_and_convert_data(url)
