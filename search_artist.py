"""
Script works with
SPotify API and helps
users with finding
information about artists
"""

import os
import base64
import json
import argparse
from typing import List
import pycountry
from requests import post, get
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

parser = argparse.ArgumentParser(description="Find the information about teh artist")
parser.add_argument('artist_name', type=str, help="Artist's name")
args = parser.parse_args()

def get_token():
    """
    Function
    """
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    """
    Functiion
    """
    return {"Authorization": "Bearer " + token}

def search_for_artist(token, artist_name):
    """
    Function
    """
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        return None
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    """
    Function
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)['tracks']
    return json_result

def get_available_markets(token: str, song_id: str):
    """
    Function
    """
    url = f"https://api.spotify.com/v1/tracks/{song_id}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result['available_markets']

def iso_to_name(iso_list: List[str]) -> List[str]:
    """
    Function
    """

if __name__ == "__main__":
    token = get_token()
    result = search_for_artist(token, args.artist_name)