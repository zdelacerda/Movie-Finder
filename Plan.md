## Program Plan
**Goal 1**: Send alert when potentially interesting movie is playing at my favorite cinema

**Goal 2**: Predict my rating for any given movie

**UI**: Web or mobile app?

**Notifcations**: Text or Email?

## Functionality
1. Open
   * Scrape from IMDb using OMDb API and Beautiful Soup
     - Overall user ratings
     - My user ratings
     - Box office movies from favorite theater
2. Read
  * Feed data into training model
3. Write
  *Send notification when interesting movie found*


## TODO
1. Find machine learning algorithm for movie predictions
2. Retrieve dataset from API
3. Train
4. Setup alert system
  1. Check box office movies
  2. Compare with model
  3. Send notification
5. Find a way to predict rating of given movie
