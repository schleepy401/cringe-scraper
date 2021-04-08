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
[
  "https://i.redd.it/randommeme1.jpg",
  "https://i.redd.it/randommeme2.jpg",
  "https://i.redd.it/randommeme3.jpg",
  ...
]
```
- **Datapoints:**
  - As of now, the API only returns a JSON array of links since I just wanted to build a simple API for testing purposes.
  ```
  [
    <String>,
    <String>,
    .... <more strings>
  ]
  ```
  - Each object in the JSON array is a string, a URL to some image/meme.

## Changelog
- **Version 1.0:**
  - *Date of release:* 4th April, 2021
  - First version of Cringe scraping API.
  - *Bugs with the current version:* None yet, just that more parameters and keys are to be added.

<!-- TODO
## Build your own API using this source code
-->

## Acknowledgments
- Documentations of the above linked technologies for being my source of learning.
- My friends for shamelessly having my back.
