# Author: Zephren de la Cerda

import requests
import json

# Constants
OMDbkey = "a542cac9"
OMDblink = "http://www.omdbapi.com/?apikey=" + OMDbkey

def getmoviebytitle(title):
    print("Getting movie.")
    response = requests.get(OMDblink + "&t=" + title)
    if (response.status_code) != 200:
        print("Get unsuccessful. Error with 'by title' get request status code: ", response.status_code)
        return null
    
    print("Get successful.")
    movie_json = response.json()
    
    print("Printing movie json string.")
    jprint(movie_json)
    
    return movie_json


    
    
def jprint(obj):
    # create formatted string from JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)   
    
getmoviebytitle("The Dark Knight")