import requests

##Eventually I'd like to use Pillow to save the images 
##from this API request
#from Pillow import Image

endpoint = "https://api.nasa.gov/planetary/apod"
# Replace DEMO_KEY below with your own key if you generated one.
api_key = "DEMO_KEY"
query_params = {"api_key": api_key} #See API Documentation to add more parameters https://api.nasa.gov
response = requests.get(endpoint, params=query_params)

#Identify the High Def photo url
photoURL = response.json()["hdurl"]
#Identify photo title
title = response.json()["title"]
print(title)

#Save the file
local_file = open('local_file.jpg', 'wb')
resp = requests.get(photoURL, stream=True)
local_file.write(resp.content)
local_file.close()
#'''not sure how to use the title of the picture as the file name'''
