import praw
from flask import Flask, jsonify
import json

app = Flask(__name__)

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

    print("Returned cringe is ", len(urls), " times cringey")
    outputData = { "data": outputJson}
    return jsonify(outputData)

@app.route('/custom')
def custom():
    try:
        num = request.args.get('n')
        subs = request.args.get('sub')

        if subs is None:
            print('subs is null')
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

        elif num is None:
            print('num is null')
            subList = subs.split(",")
            for sub in subList:
                myPosts = redditwa.subreddit(sub).hot(limit = 10)
                for post in myPosts:
                    if ".jpg" in post.url:
                        urls.append(post.url)
                        permalinks.append(post.permalink)
                        titles.append(post.title)
                        authors.append(post.author)
                        structure = { "author": str(authors[len(authors) - 1]), "title": str(titles[len(titles) - 1]), "url": str(urls[len(urls) - 1]), "permalink": str(permalinks[len(permalinks) - 1]) }
                        outputJson.append(structure)

        elif num is None and subs is None:
            error = {"data" : "404. Please enter in the correct format. Consult docs at https://github.com/w0lfw1tz/cringe-scraper" }
            return jsonify(error)

        else:
            subList = subs.split(",")
            print(subList)
            for sub in subList:
                myPosts = redditwa.subreddit(sub).hot(limit = int(num))
                for post in myPosts:
                    if ".jpg" in post.url:
                        urls.append(post.url)
                        permalinks.append(post.permalink)
                        titles.append(post.title)
                        authors.append(post.author)
                        structure = { "author": str(authors[len(authors) - 1]), "title": str(titles[len(titles) - 1]), "url": str(urls[len(urls) - 1]), "permalink": str(permalinks[len(permalinks) - 1]) }
                        outputJson.append(structure)


        print("Returned cringe is ", len(urls), " times cringey")
        outputData = { "data": outputJson}
        if len(urls) is 0:
            return jsonify({"data" : "40x no images found"})
        return jsonify(outputData)

    except:
        traceback.print_exc()
        error = {"data" : "404. Please enter in the correct format. Consult docs at https://github.com/w0lfw1tz/cringe-scraper" }
        return jsonify(error)
