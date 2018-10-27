import requests
import json


def get_access_token(client_id, client_secret, refresh_token):
    url = 'https://www.googleapis.com/oauth2/v4/token'

    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }

    response = requests.post(
        url=url,
        data=data
    )

    return response.json().get('access_token')


def get_video_ids_in_playlist(playlist_id, access_token, max_results=50):
    url = 'https://www.googleapis.com/youtube/v3/playlistItems'

    params = {
        'part': 'contentDetails',
        'playlistId': playlist_id,
        'maxResults': max_results
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(access_token)
    }

    response = requests.get(
        url=url,
        params=params,
        headers=headers
    )

    return [
        video['contentDetails']['videoId'] for video in response.json()['items']
    ]


def add_video_to_playlist(playlist_id, video_id, access_token):
    url = 'https://www.googleapis.com/youtube/v3/playlistItems'

    params = {
        'part': 'snippet'
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(access_token)
    }

    data = {
        'snippet': {
            'playlistId': playlist_id,
            'resourceId': {
                'kind': 'youtube#video',
                'videoId': video_id
            },
        }
    }

    requests.post(
        url=url,
        params=params,
        headers=headers,
        data=json.dumps(data)
    )
