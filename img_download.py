# creating object
from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()

def downloadimages(query):
    # keywords is the search query
    # format is the image file format
    # limit is the number of images to be downloaded
    # print urs is to print the image file url
    # size is the image size which can
    # be specified manually ("large, medium, icon")
    # aspect ratio denotes the height width ratio
    # of images to download. ("tall, square, wide, panoramic")
    arguments = {"keywords": query, "limit": 1}
    try:
        response.download(arguments)
        print("worked")

    # Handling File NotFound Error
    except FileNotFoundError:
        print("error not fatal")
        arguments = {"keywords": query, "limit": 1}

        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments)
        except:
            print("error fatal")
