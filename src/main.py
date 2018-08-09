import os
from praw import Reddit
from dotenv import load_dotenv
from src.youtube import get_access_token, add_video_to_playlist, get_video_ids_in_playlist
from src.reddit import extract_video_ids_from_subreddit


def get_video_ids():
    reddit = Reddit(
        client_id=os.environ['REDDIT_CLIENT_ID'],
        client_secret=os.environ['REDDIT_CLIENT_SECRET'],
        user_agent='Script User Agent'
    )

    subreddit_name = os.environ['REDDIT_SUBREDDIT']
    subreddit = reddit.subreddit(subreddit_name)

    return extract_video_ids_from_subreddit(subreddit)


def add_videos_to_playlist(video_ids):
    access_token = get_access_token(
        client_id=os.environ['YOUTUBE_CLIENT_ID'],
        client_secret=os.environ['YOUTUBE_CLIENT_SECRET'],
        refresh_token=os.environ['YOUTUBE_REFRESH_TOKEN']
    )

    playlist_id = os.environ['YOUTUBE_PLAYLIST_ID']

    video_ids_in_playlist = get_video_ids_in_playlist(playlist_id, access_token)

    # don't add duplicates (= already in playlist)
    for video_id in [v for v in video_ids if v not in video_ids_in_playlist]:
        add_video_to_playlist(
            playlist_id,
            video_id,
            access_token
        )


def work():
    load_dotenv()

    video_ids = get_video_ids()
    add_videos_to_playlist(video_ids)


if __name__ == "__main__":
    work()
