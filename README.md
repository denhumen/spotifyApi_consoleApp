# Spotify Console App
  This is a simple console app that allows users to search for an artist on Spotify and get their full name, top 5 most popular songs, artist ID, and available country markets for their most popular song.

## Getting Started
Prerequisites
To use this app, you will need to have the following:

1. A Spotify account
2. A registered Spotify application with client ID and client secret
3. Python installed on your machine

## Installing
1. Clone this repository to your local machine.
2. Run npm install to install the necessary dependencies.
3. Open a .env file in the root directory and add your Spotify client ID and secret:

'''css
SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here
'''

## Running the App
1. Open your terminal or command prompt and navigate to the root directory of the app.
1. Run this command to start the app:
'''css
python search_artist.py <name_of_the_artist>
'''
Follow the prompts to search for an artist.
Built With
Python
Spotify Web API - Music streaming service API
## Authors
Denis Humeniuk - initial work
## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
