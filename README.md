# Word Search Generator

### Deployment

[Live App](https://word-search-generator.netlify.com/) on Netlify

[Client Repo](https://github.com/MorganHuegel/word-search-generator-client)


### Description

This is a web application where a user can input a list of words and puzzle dimensions, and the app will generate an NxN square
word-search.  The word-search is formatted into HTML and displayed on the screen for the user. See client repo and live app
for details.

### API Documentation

#### GET all puzzles
  - Request Type: `GET`
  - Path: `https://word-search-generator-server.herokuapp.com/puzzles/`
  - JSON Response Body: 
  ```
  [
    {
        "id": 2,
        "title": "States",
        "words": [
            "pennsylvania",
            "vermont",
            "wyoming",
            "newyork",
            "florida",
            "arizona",
            "oregon",
            "michigan"
        ]
    },
    {
        "id": 1,
        "title": "Animals",
        "words": [
            "frog",
            "chimp",
            "walrus",
            "pelican",
            "deer",
            "sasquatch",
            "horse"
        ]
    }
  ] 
  ```
  
  
#### GET one puzzles
  - Request Type: `GET`
  - Path: `https://word-search-generator-server.herokuapp.com/puzzles/puzzleIdInteger/`
  - JSON Response Body:
  ```
  {
    "id": 1,
    "title": "Animals",
    "words": [
        "frog",
        "chimp",
        "walrus",
        "pelican",
        "deer",
        "sasquatch",
        "horse"
    ],
    "puzzle": [
        ["w", "o", "f", "p", "s", "q", "e", "o", "n", "t", "s", "l", "z", "i", "l"],
        ["u", "n", "s", "e", "a", "m", "i", "w", "t", "o", "u", "m", "k", "d", "g"],
        ["s", "o", "a", "a", "s", "b", "a", "r", "s", "i", "r", "u", "t", "g", "e"],
        ["h", "l", "m", "o", "q", "c", "e", "m", "c", "l", "l", "v", "n", "o", "g"],
        ["b", "f", "i", "g", "u", "f", "u", "g", "m", "u", "a", "p", "n", "o", "x"],
        ["u", "h", "w", "l", "a", "r", "t", "j", "p", "v", "w", "u", "b", "n", "l"],
        ["k", "t", "r", "s", "t", "o", "f", "o", "f", "e", "b", "g", "j", "a", "q"],
        ["y", "e", "t", "q", "c", "g", "m", "c", "o", "e", "l", "k", "i", "b", "g"],
        ["g", "q", "z", "l", "h", "q", "j", "h", "k", "y", "s", "h", "a", "p", "e"],
        ["w", "k", "h", "o", "l", "h", "z", "i", "v", "n", "k", "d", "d", "k", "l"],
        ["r", "v", "d", "z", "z", "e", "e", "m", "f", "p", "h", "g", "r", "d", "i"],
        ["p", "n", "l", "a", "t", "y", "u", "p", "e", "u", "l", "a", "g", "n", "g"],
        ["e", "s", "r", "o", "h", "r", "e", "e", "d", "m", "j", "k", "i", "s", "o"],
        ["y", "j", "k", "v", "c", "e", "h", "r", "j", "r", "v", "z", "i", "s", "p"],
        ["x", "w", "p", "e", "l", "i", "c", "a", "n", "t", "x", "o", "v", "s", "m"]
    ]
  }
  ```


### Key code snippets

To check the algorithm used to generate each word-search, checkout [./word_search/algorithm.py](https://github.com/MorganHuegel/word-search-generator-server/blob/master/word_search/algorithm.py) 
or checkout [this repo](https://github.com/MorganHuegel/word-search-algorithm)

Other key points of this code are the [database models](https://github.com/MorganHuegel/word-search-generator-server/blob/master/word_search/models.py) 
(set up for a SQL database, but Django uses a ORM to query it) 
and the http [request endpoints](https://github.com/MorganHuegel/word-search-generator-server/blob/master/word_search/views.py)

