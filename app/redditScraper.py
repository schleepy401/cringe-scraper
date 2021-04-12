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


@app.route('/', methods = ['GET'])
def home():
    for sub in subReddits:
        myPosts = redditwa.subreddit(sub).hot(limit = 10)
        for post in myPosts:
            if ".jpg" in post.url:
                urls.append(post.url)
                permalinks.append(post.permalink)
                titles.append(post.title)
                authors.append(post.author)
                structure = { "author": str(authors[len(authors) - 1]), "title": str(titles[len(titles) - 1]), "url": str(urls[len(urls) - 1]), "permalink": str(permalinks[len(permalinks) - 1]) }
                outputJson.append(structure)

    outputData = { "data": outputJson}
    return jsonify(outputData)

@app.route('/custom')
def res():
    num = request.args.get('n')

    for sub in subReddits:
        myPosts = redditwa.subreddit(sub).hot(limit = int(num))
        for post in myPosts:
            if ".jpg" in post.url:
                urls.append(post.url)
                permalinks.append(post.permalink)
                titles.append(post.title)
                authors.append(post.author)
                structure = { "author": str(authors[len(authors) - 1]), "title": str(titles[len(titles) - 1]), "url": str(urls[len(urls) - 1]), "permalink": str(permalinks[len(permalinks) - 1]) }
                outputJson.append(structure)

    outputData = { "data": outputJson}
    return jsonify(outputData)

if __name__=="__main__":
	app.run()


    return jsonify(urls)
