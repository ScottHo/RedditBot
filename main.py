import praw

if __name__  == "__main__":
    reddit = praw.Reddit(client_id="uGEGWTEENyDUXw",
            client_secret="E_k7BbR7PON__YlBpWuQmwwRRag",
            user_agent="My Reddit Bot v0.1")
    subreddit = reddit.subreddit('AskReddit')
    for submission in subreddit.hot(limit=10):
        print(submission.title)
