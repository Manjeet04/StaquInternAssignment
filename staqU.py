# Staqu Summer Intern Assignment
# Code to extract all videos of a channel with 5 similar videos of each video.
# Created by : Manjeet Singh
# Created on : 19 March 2018

# for handling get requests.
import requests
import sys

# input of channel
channelId = raw_input("Enter the channel Id you wish videos for : ")

# Initial API hit to get upload Id to further fetch playlist
URL1 = "https://www.googleapis.com/youtube/v3/channels"
PARAMS1 = {'id': channelId, 'part' : "contentDetails",'key': 'AIzaSyC6Lus6uknBzSQY7Feo1Eoi_cKLCDgS1sA'}
r = requests.get(url = URL1, params = PARAMS1)
data = r.json()

# Check for validation of channel ID.
if data['pageInfo']['totalResults'] == 0:
    print "Invalid channel id"
    sys.exit()
    

# fetching upload ID
upload_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# API-2 to fetch all the playlist of the channel
URL2 = "https://www.googleapis.com/youtube/v3/playlistItems"
PARAMS2 = {'playlistId': upload_id, 'part' : "snippet",'key': 'AIzaSyC6Lus6uknBzSQY7Feo1Eoi_cKLCDgS1sA'}
r = requests.get(url = URL2, params = PARAMS2)
data = r.json()

count = 0

# Infinite loop till no next page is encountered.
while(1):
    
    next_page_token = data['nextPageToken']
    total_items = data['items']
    for i in total_items :

         # Printing all the fetched videos information
         count = count+1
         video_id  = i['snippet']['resourceId']['videoId']
         print "The video id %d is :"%(count)
         print video_id
         print "\n"
         print "The video title is :"
         print i['snippet']['title']
         print "\n"
         print "The video description is :"
         print i['snippet']['description']
         print "\n"
         print "\n"
         print "\n"
         print "The 5 videos related to this video are :"

         # API-3 to fetch similar 5 videos of the video
         URL3 = "https://www.googleapis.com/youtube/v3/search"
         PARAMS3 = {'relatedToVideoId': video_id, 'part' : "snippet",'key': 'AIzaSyC6Lus6uknBzSQY7Feo1Eoi_cKLCDgS1sA','type':'video'}
         r = requests.get(url = URL2, params = PARAMS2)
         data = r.json()
         total_items = data['items']
         count1 = 0
         for j in total_items :

                  # Printing similar video information.
                  video_id  = j['snippet']['resourceId']['videoId']
                  print "\tThe video id %d is :"%(count1+1)
                  print "\t",video_id
                  print "\n"
                  print "\tThe video title is : "
                  print "\t",j['snippet']['title']
                  print "\n"
                  print "\tThe video description is : "
                  print "\t",j['snippet']['description']
                  print "\n"
                  print "\tThe channel title is : "
                  print "\t",j['snippet']['channelTitle']
                  print "\n"
                  print "\n"
                  count1 = count1+1
         
         print "\n\n\n"
         
    # API hit to get next page videos     
    PARAMS2 = {'playlistId': upload_id, 'part' : "snippet",'key': 'AIzaSyC6Lus6uknBzSQY7Feo1Eoi_cKLCDgS1sA','pageToken' : next_page_token }
    r = requests.get(url = URL2, params = PARAMS2)
    data = r.json()

    # Break if no next page is left.
    if 'nextPageToken' not in data:
        break
    
# Printing total number of videos of channel
print "Total number of videos in requested channel are : ",count



