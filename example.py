import praw, reddit2md, settings

reddit = praw.Reddit(
                client_id = settings.credentials['client_id'],
                client_secret = settings.credentials['client_secret'],
                user_agent = settings.credentials['user_agent'],
            )

# reddit.config.decode_html_entities = True # Consider decoding HTML as some of the HTML entities might show up undecoded.

posts = reddit.subreddit('learnpython').hot(limit=5)

for post in posts:
    reddit2md.r2md(post, timezone='Asia/Seoul')