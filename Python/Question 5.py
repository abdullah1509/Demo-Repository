import requests


def download_and_extract_data(url):
    # Download the data from the API link
    response = requests.get(url)
    data = response.json()

    # Extract the required data
    show_name = data.get('name', '')
    premiered = data.get('premiered', '')
    language = data.get('language', '')
    genres = ', '.join(data.get('genres', []))

    print("Show Name:", show_name)
    print("Premiered:", premiered)
    print("Language:", language)
    print("Genres:", genres)

    # Extract episode information
    episodes = data.get('_embedded', {}).get('episodes', [])
    if episodes:
        print("Episodes:")
        for episode in episodes:
            episode_name = episode.get('name', '')
            episode_season = episode.get('season', '')
            episode_number = episode.get('number', '')
            print("  - Episode:", episode_name)
            print("    Season:", episode_season)
            print("    Number:", episode_number)
            print()


# Provide the API link to download the data from
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Call the function to download and extract the data
download_and_extract_data(url)
