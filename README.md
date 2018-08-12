## reddit2youtube

- Adds all posted Youtube videos in a Subreddit to a Youtube playlist.
- AWS Lambda function, built with [Zappa](https://github.com/Miserlou/Zappa).
- Runs every 30 minutes (see `zappa_settings.json`)

### Install & deploy
    pipenv install && pipenv shell

    # edit & move .env.default → .env
    zappa deploy production

### Run tests
    python -m unittest

### Getting an OAuth2 refresh token for Youtube
    https://stackoverflow.com/a/41556775/3774227
