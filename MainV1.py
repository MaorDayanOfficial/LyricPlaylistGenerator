import requests
import random

# Configure your API credentials
CLIENT_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
HEADERS = {'Authorization': 'Bearer ' + CLIENT_ACCESS_TOKEN}
BASE_URL = 'https://api.genius.com'

# Search songs based on specific themes, moods, or genres using lyrics as input
def search_songs_by_lyrics(search_query):
    endpoint = f'{BASE_URL}/search'
    params = {
        'q': search_query
    }
    response = requests.get(endpoint, headers=HEADERS, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['response']['hits']
    else:
        print('Error occurred while searching for songs.')
        return None

# Generate a playlist based on the search results
def generate_playlist(search_results, playlist_length):
    if len(search_results) == 0:
        print('No songs found for the given search query.')
        return

    playlist = random.sample(search_results, min(playlist_length, len(search_results)))
    print('Generated Playlist:')
    for index, song in enumerate(playlist, start=1):
        title = song['result']['title']
        artist = song['result']['primary_artist']['name']
        print(f'{index}. {title} - {artist}')
    print()

# Main function
def main():
    # Prompt user to enter the search query
    search_query = input('Enter a search query based on themes, moods, or genres: ')

    # Prompt user to enter the desired playlist length
    playlist_length = int(input('Enter the desired playlist length: '))

    # Search songs based on the given search query
    search_results = search_songs_by_lyrics(search_query)

    if search_results:
        # Generate a playlist based on the search results
        generate_playlist(search_results, playlist_length)

# Execute the script
if __name__ == '__main__':
    main()
