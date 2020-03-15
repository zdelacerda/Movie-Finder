## Program Plan
**Goal 1**. Send alert when potentially interesting movie is playing at my favorite cinema

**Goal 2**. Predict my rating for any given movie

## Functionality
1. **Get**
   * Scrape from IMDb using OMDb API and Beautiful Soup
     - Overall user ratings
     - My user ratings
     - Box office movies from favorite theater
2. **Evaluate**
    1. *Content-based: if you like an item, then you will also like a "similar" item
      * Flow: input=newMovie -> return=listOfRelatedMovies ~ compare list with users list of movies/ratings for result
    2. Item-Item Collaborative Filtering: find movie's look-alike, reccomend alike movies to the user
    
3. **Return**
    * Send notification when interesting movie found


## TODO
1. **UI**: Web or mobile app?
7. **Notifcations**: Text or Email?Find machine learning algorithm for movie predictions
2. Retrieve dataset from API
4. Setup alert system
    - Check box office movies
    - Compare with model
    - Send notification
5. Find a way to predict rating of given movie

