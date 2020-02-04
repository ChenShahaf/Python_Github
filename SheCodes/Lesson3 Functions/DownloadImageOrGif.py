'''
Lecture 3 - Download a pic from the internet - X Files
1. the function randomize a number between 1 to 1K
2. the number will be added a .png or .jpg at the end
3. we will import the module urllib.request
4. we will call the function urlretrieve - 4 parameters, 2 will be defult of None
5. we will use the urlretrieve to get the picture
'''

#import functions
import urllib.request
import urllib.parse
from random import *

#defining the function for downloading a picture
def download_web_image():
    rand_num = randint(1, 1000)
    # URL Of the Picture - change according to will
    #url = 'https://upload.wikimedia.org/wikipedia/en/e/e1/Thexfiles.jpg'
    url = 'https://media.giphy.com/media/10RhccNxPSaglW/giphy.gif'
    #reason to give a random number since images downloaded usually get random numbers
    full_name = "CAT" + str(rand_num) + ".gif"

    #downloading the image
    #urllib.request.urlretrieve(url, full_name, reporthook= None, data = None)

    #Alternative way
    path = 'C:/Users/Chen/PycharmProjects/TESTPYTHON/'
    urllib.request.urlretrieve(url, path + full_name)

download_web_image()
