# Word Search Generator

### Deployment

[Live App](https://word-search-generator.netlify.com/) on Netlify

[Client Repo](https://github.com/MorganHuegel/word-search-generator-client)


### Description

This is a web application where a user can input a list of words and puzzle dimensions, and the app will generate an NxN square
word-search.  The word-search is formatted into HTML and displayed on the screen for the user. See client repo and live app
for details.


### Key code snippets

To check the algorithm used to generate each word-search, checkout [./word_search/algorithm.py](https://github.com/MorganHuegel/word-search-generator-server/blob/master/word_search/algorithm.py) 
or checkout [this repo](https://github.com/MorganHuegel/word-search-algorithm)

Other key points of this code are the [database models](https://github.com/MorganHuegel/word-search-generator-server/blob/master/word_search/models.py) 
(set up for a SQL database, but Django uses a ORM to query it) 
and the http [request endpoints](https://github.com/MorganHuegel/word-search-generator-server/blob/master/word_search/views.py)

