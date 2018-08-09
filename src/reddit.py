import re

video_id_regex = re.compile(
    r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/' +
    '(watch\?v=|embed/|v/|.+\?v=)?(?P<video_id>[A-Za-z0-9\-=_]{11})'
)


def extract_video_id_from_url(url):
    match = video_id_regex.match(url)

    if match:
        return match.group('video_id')


def extract_video_ids_from_subreddit(subreddit, limit=50):
    video_ids = []

    for submission in subreddit.new(limit=limit):
        extracted_video_id = extract_video_id_from_url(submission.url)

        if extracted_video_id is not None:
            video_ids.append(extracted_video_id)

    return video_ids
