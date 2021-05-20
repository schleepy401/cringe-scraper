# cringe-scraper
A Reddit scraping API which began as a cringe subs scraping bot hence the name.

## Table of Contents
<!-- TABLE OF CONTENTS -->
  <ol>
    <li>
      <a href="#features">Features</a>
    </li>
    <li>
      <a href="#using-the-api">Using the API</a>
      <ol>
      <li>
        <a href="#datapoints">Datapoints</a>
      </li>
      <li>
        <a href="#making-custom-requests">Making custom requests</a>
      </li>
      </ol>
    </li>
    <li>
      <a href="#changelog">Changelog</a>
      <ol>
      <li>
        <a href="#version-10">Version 1.0 (4th April 2021)</a>
      </li>
      <li>
        <a href="#version-20">Version 2.0 (13th April 2021)</a>
      </li>
      <li>
        <a href="#version-30">Version 3.0 (21st May 2021)</a>
      </li>
      </ol>
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
- **Default Subreddits being scraped:** [r/sadcringe](https://reddit.com/r/sadcringe), [r/SadMemesForHipTeens](https://reddit.com/r/SadMemesForHipTeens), [r/CringeTopia](https://reddit.com/r/CringeTopia), [r/sadmemes](https://reddit.com/r/sadmemes)
- **API is live at** [this link](https://cringescraper.herokuapp.com)
- Supports **custom subreddits search** and **custom number of posts** (default is 10). See <a href="#making-custom-requests">Making Custom Requests</a> section for more information.
- The data is returned in JSON format. Feel free to use this in your apps or projects.

## Using the API
- Just call the link [https://cringescraper.herokuapp.com](https://cringescraper.herokuapp.com). The API will return a data in the following format:
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
### Datapoints
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
### Making custom requests
  - The API currently supports two arguments for custom requests after the ```/custom?``` path:
    - ```n``` (No. of requested posts): The number of memes you request the API to scrape. Returns the posts which are images out of the scraped ones. Default is 10.
    - ```sub``` (Subreddits to search): The subreddits you request the API to scrape. Default subreddits are listed above.
  - Example of using custom requests: [https://cringescraper.herokuapp.com/custom?sub=sadcringe,memes&n=5](https://cringescraper.herokuapp.com/custom?sub=sadcringe,memes&n=5) gives the output:
  ```
  {
  "data": [
    {
      "author": "merothecat",
      "permalink": "/r/sadcringe/comments/nh02q2/down_horrendous/",
      "title": "Down horrendous",
      "url": "https://i.redd.it/bgxrorjs0a071.jpg"
    },
    {
      "author": "bearpilot",
      "permalink": "/r/sadcringe/comments/ngt2ni/not_like_ive_eaten_it_yet/",
      "title": "not like I’ve eaten it yet 😂",
      "url": "https://i.imgur.com/rSgQFPN.jpg"
    },
    {
      "author": "tonybinky20",
      "permalink": "/r/sadcringe/comments/nh1tiz/one_of_the_worst_twitter_threads_ive_ever_read/",
      "title": "One of the worst Twitter threads I’ve ever read",
      "url": "https://i.redd.it/ilds7cslda071.jpg"
    },
    {
      "author": "Boernator",
      "permalink": "/r/sadcringe/comments/ng8avl/why_would_you_trust_some_random_billionaire/",
      "title": "Why would you trust some random billionaire?",
      "url": "https://i.redd.it/piqgu5tle3071.jpg"
    },
    {
      "author": "lobofett12",
      "permalink": "/r/memes/comments/nghvge/be_original_original_wednesday_frog_memes_are_not/",
      "title": "Be Original. Original Wednesday frog memes are not banned, The two exact copies of these are just reposts. Reposts have always been against the rules. Edits of these are allowed.",
      "url": "https://i.redd.it/4qy2tdptb5071.jpg"
    },
    {
      "author": "Tyja136",
      "permalink": "/r/memes/comments/ngz69l/multitasking_ftw/",
      "title": "Multitasking ftw.",
      "url": "https://i.redd.it/u3e2pwbpt9071.jpg"
    }
  ]
}
  ```
  - **WARNING**: *Using atleast one parameter is compulsory else the API will return an error message.*
## Changelog
### Version 1.0
  - *Date of release:* 4th April, 2021
  - First version of Cringe scraping API.
  - *Bugs with the current version:* None yet, just that more parameters and keys are to be added.

### Version 2.0
  - *Date of release:* 13th April, 2021
  - *New features with this build:*
    - The API now supports **custom requests** for a specific number of memes per subreddit! Go ahead, check it out now, but first check the docs.
    - **WARNING**: The API has been reorganised in a new format for the datapoints so old apps/things parsing the old way may not work. The documentation has been updated.
  - *Bugs with the current version:*
    - The custom requests thing doesn't return the exact correct number of memes as of now.
    - The memes may not be randomised, this only returns reddit posts from the hot posts feed of the subreddits.
### Version 3.0
  - *Date of release:* 21st May, 2021
  - *New features with this build:*
    - The API now supports custom subreddit search via the argument ```sub```. Please check the <a href="#making-custom-requests">Making Custom Requests</a> section for more information.
  - *Bugs with the current version:*
    - There are still bugs with the randomisation of memes and exact meme numbering. Working on it as well.
<!-- TODO
## Build your own API using this source code
-->

## Acknowledgments
- Documentations of the above linked technologies for being my source of learning.
- My friends for shamelessly having my back.
