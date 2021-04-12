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
### Making custom requests
  - The API currently supports custom requests for the number of memes per subreddit. For that, just add ```/custom?n=[number of memes you want]``` at the end of the original API link.
  - *Example:* Calling the API with a custom request of 5 memes per subreddit by using [https://cringescraper.herokuapp.com/custom?n=5](https://cringescraper.herokuapp.com/custom?n=5), we get:
  ```
  {
    "data":
    [
      {
        "author": "MrSluagh",
        "permalink": "/r/sadmemes/comments/mphwop/just_the_thought_of_getting_or_having_a_loved_one/",
        "title": "Just the thought of getting, or having a loved one with either disease is the scariest thing to me as you’re personality is slowly withering away.",
        "url": "https://i.redd.it/pm88fpv2urs61.jpg"
      },
      {
        "author": "hornycommunist69",
        "permalink": "/r/sadmemes/comments/mopj3l/based_on_a_true_story/",
        "title": "Based on a true story...",
        "url": "https://i.redd.it/6dfa8o607js61.jpg"
      },
      {
        "author": "GiannRYS",
        "permalink": "/r/sadmemes/comments/mozuqt/this_world_shall_know_pain/",
        "title": "this world shall know pain",
        "url": "https://i.redd.it/mawor6534ms61.jpg"
      },
      {
        "author": "MrSkeletonMan1",
        "permalink": "/r/sadcringe/comments/mp80v2/why_even_bother_living_at_this_point/",
        "title": "Why even bother living at this point?",
        "url": "https://i.redd.it/618jlch0pos61.jpg"
      },
      {
        "author": "b4a4",
        "permalink": "/r/sadcringe/comments/mpa5wo/i_donno_what_to_say/",
        "title": "i donno what to say",
        "url": "https://i.redd.it/1y9o19jgmps61.jpg"
      },
      {
        "author": "agrandthing",
        "permalink": "/r/sadcringe/comments/mp093y/this_pitiful_piece_of_insanity_on_my_street/",
        "title": "This pitiful piece of insanity on my street",
        "url": "https://i.redd.it/w9eyr1pv7ms61.jpg"
      },
      {
        "author": "LolEccsDee",
        "permalink": "/r/sadcringe/comments/mpc675/homies_down_bad/",
        "title": "Homies down bad",
        "url": "https://i.imgur.com/Dk9p0ab.jpg"
      },
      {
        "author": "dope_ass_freshprince",
        "permalink": "/r/SadMemesForHipTeens/comments/mpigb3/flawed_by_chris_w/",
        "title": "Flawed by Chris w.❤",
        "url": "https://i.redd.it/hkw7rx3izrs61.jpg"
      },
      {
        "author": "chromeir",
        "permalink": "/r/SadMemesForHipTeens/comments/mnf830/reality_is_painful/",
        "title": "Reality is painful",
        "url": "https://i.redd.it/9n4aq610w4s61.jpg"
      },
      {
        "author": "None",
        "permalink": "/r/SadMemesForHipTeens/comments/mmms28/parmesan/",
        "title": "parmesan",
        "url": "https://i.redd.it/pi8scqrahvr61.jpg"
      },
      {
        "author": "KentoPento",
        "permalink": "/r/Cringetopia/comments/mpgprg/5_minute_crafts_is_taking_over_the_sub/",
        "title": "5 Minute Crafts is taking over the sub.",
        "url": "https://i.redd.it/3rvpqr7xkrs61.jpg"
      },
      {
        "author": "N1111C4",
        "permalink": "/r/Cringetopia/comments/mpdv83/meta_meme/",
        "title": "Meta meme",
        "url": "https://i.redd.it/e4s863yhvqs61.jpg"
      }
    ]
  }
  ```
  - **NOTE:** The above response was generated the day I made the first commit for the custom requests code, hence the output is not perfect yet. It will be corrected in the coming days.

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
