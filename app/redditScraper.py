import praw
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    reddit_obj = praw.Reddit(
        client_id = "your-client-id-here",
        client_secret = "your-client-secret-here",
        user_agent = "your-agent-here"
        )

    authors = []
    titles = []
    urls = []
    permalinks = []
    subReddits = ['your', 'choice', 'of', 'subreddits', 'here']

    for sub in subReddits:
        myPosts = reddit_obj.subreddit(sub).hot()
        for post in myPosts:
            if "comments" not in post.url:
                urls.append(post.url)

    return jsonify(urls)
