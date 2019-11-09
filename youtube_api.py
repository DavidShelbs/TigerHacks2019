from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
import matplotlib.pyplot as plt

DEVELOPER_KEY = "AIzaSyDW8VQHj6hgGhdPQwy-hlzU7JGPMCTfPzk"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

def search(query, max_results=1, order="relevance", token=None, location=None, location_radius=None):
    search_response = youtube.search().list(
    q=query,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet",
    maxResults=max_results,
    location=location,
    locationRadius=location_radius).execute()

    print("Search Completed...")
    print("Total results: {0} \nResults per page: {1}".format(search_response['pageInfo']['totalResults'], search_response['pageInfo']['resultsPerPage']))
    print("Example output per item, snippet")
    print(search_response['items'][0]['snippet'].keys())
    #Assign first page of results (items) to item variable
    items = search_response['items'] #50 "items"
    #Assign 1st results to title, channelId, datePublished then print
    title = items[0]['snippet']['title']
    channelId = items[0]['snippet']['channelId']
    datePublished = items[0]['snippet']['publishedAt']
    print("First result is: \n Title: {0} \n Channel ID: {1} \n Published on: {2}".format(title, channelId, datePublished))
    return search_response
