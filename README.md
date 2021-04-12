# cringe-scraper
Get random cringey memes via this.

## Table of Contents
<!-- TABLE OF CONTENTS -->
  <ol>
    <li>
      <a href="#features">Features</a>
    </li>
    <li>
      <a href="#using-the-api">Using the API</a>
    </li>
    <li>
      <a href="#changelog">Changelog</a>
    </li>
    <!-- TODO
    <li>
      <a href="#contributors">Contributors</a>
    </li>
  -->
    <li>
      <a href="#acknowledgments">Acknowledgments</a>
    </li>
  </ol>

## Features
- **Language:** [Python 3.8.5](https://docs.python.org/3.8/)
- **Technologies used:**
  - [PRAW: The Python Reddit API Wrapper](https://pypi.org/project/praw/)
  - [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
- **Subreddits being scraped:** [r/sadcringe](https://reddit.com/r/sadcringe), [r/SadMemesForHipTeens](https://reddit.com/r/SadMemesForHipTeens), [r/CringeTopia](https://reddit.com/r/CringeTopia), [r/sadmemes](https://reddit.com/r/sadmemes)
- **API is live at** [this link](https://cringescraper.herokuapp.com)
- The data is returned in JSON format. Feel free to use this in your apps or projects.

## Using the API
- Just call the link [https://cringescraper.herokuapp.com](https://cringecraper.herokuapp.com). The API will return a data in the following format:
```
{
  "data":
    [ # JSON Array
      {
        "author": <String>,
        "permalink": <String>,
        "title": <String>,
        "url": <String>
      },
      {
        "author": <String>,
        "permalink": <String>,
        "title": <String>,
        "url": <String>
      },
      ...
    ]
}
```
- **Datapoints:**
  - The API returns a JSON object in the following format:
  ```
  {
    "data":
      [ # JSON Array
        {
          "author": <String>,
          "permalink": <String>,
          "title": <String>,
          "url": <String>
        },
        {
          "author": <String>,
          "permalink": <String>,
          "title": <String>,
          "url": <String>
        },
        ...
      ]
   }
  ```
  - *"data":* The first key in the JSON houses the JSON array of responses. The JSON array houses the child JSON objects as shown above. The datapoints in the JSON objects are explained below.
  - *"author":* A string which returns the username of the original poster from reddit.
  - *"permalink":* A string which returns a reddit permalink of the following format: ```"/r/subReddit/comments/userid/post_name_or_title_in_short"```. Can be used to share it or view the original post on reddit via proper decoration, i.e. adding ```"reddit.com/"``` in front of the permalink.
  - *"title":* A string which returns the title of the original post.

## Changelog
- **Version 1.0:**
  - *Date of release:* 4th April, 2021
  - First version of Cringe scraping API.
  - *Bugs with the current version:* None yet, just that more parameters and keys are to be added.

- **Version 2.0:**
  - *Date of release:* 13th April, 2021
  - *New features with this build:*
    - The API now supports **custom requests** for a specific number of memes per subreddit! Go ahead, check it out now, but first check the docs.
    - **WARNING**: The API has been reorganised in a new format for the datapoints so old apps/things parsing the old way may not work. The documentation has been updated.
  - *Bugs with the current version:*
    - The custom requests thing doesn't return the exact correct number of memes as of now.
    - The memes may not be randomised, this only returns reddit posts from the hot posts feed of the subreddits.
<!-- TODO
## Build your own API using this source code
-->

## Acknowledgments
- Documentations of the above linked technologies for being my source of learning.
- My friends for shamelessly having my back.
