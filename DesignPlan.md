## Design Plan

****

### High Level Flow
Input user data -> process data/save to userID -> create MovieReferralSystem -> scan box-office movies daily -> if match is found send SMS with movie details

### Mid Level Flow
Input IMDB account, phone number, name, location -> create user entity with input -> parse IMDB into data -> feed data into model/algorithm -> scan box-office movies -> compare with MovieReferralSystem -> send SMS

### Low Level Flow
Input IMDB account, phone number, name, location/favorite movie theater -> create user account with input -> parse IMDB database (weekly) into local user data -> webs scrap (local/favorite)theaters for current box-office movie list (daily) -> run algorithm to compare each new box-office movie with user data (daily) -> send SMS with movie name, reasons for interest, link to trailer, link to regal app/showtimes

****

## Components
1. **Messaging** - Find a way to send SMS messages 
2. **User account creation/database** - storage for user personal information + movie preferences (updated weekly)
3. **IMDB API** - web scrape IMDB 'your ratings' and parse into database/hashmap
4. **Box office** - web scrape local theater box-office for list of movies + movie attributes
5. **MovieReferralAlgorithm** - algorithm that compares movie cast, director, genre, ratings, etc from user history with box office titles
6. **Timer** - weekly IDMB pulls + database updates, daily box office pulls + referral checks
7. **Web App** - web interface for application

****

## Functionality
1. **Web Scraping**
   * Scrape from IMDb using OMDb API and Beautiful Soup
     - Overall user ratings
     - My user ratings
     - Box office movies from favorite theater

****

## Resources:
### General
[Open Movie Database API](http://www.omdbapi.com/)

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

[Python API Tutorial](https://www.dataquest.io/blog/python-api-tutorial/)

### Machine Learning
[*4 Rengines to Predict Movie Taste](https://towardsdatascience.com/the-4-recommendation-engines-that-can-predict-your-movie-tastes-109dc4e10c52)

[Movie Rating Prediction Example](https://www.kaggle.com/sherinclaudia/movie-rating-prediction/notebook/)

[Collaborative Filtering](https://codeburst.io/explanation-of-recommender-systems-in-information-retrieval-13077e1d916c)

[!Movie Reccomendation System (requries list of users)](https://towardsdatascience.com/fast-ai-season-1-episode-5-1-movie-recommendation-using-fastai-a53ed8e41269)


### Web Scraping
[Soup with IMDb example](https://www.dataquest.io/blog/web-scraping-beautifulsoup/)

[*Better IMDb example](https://medium.com/@kimdang229/python-and-beautifulsoup-web-scraping-tutorial-1d47e7a38fab)