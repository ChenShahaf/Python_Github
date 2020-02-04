'''
Lecture 3 - Download a pic from the internet -SHECODES
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
def download_web_image(url):
    name = randint(1, 1000)
    #alternative way to write the same line
    #name = random.randrange(1, 1000)
    #reason to give a random number since images downloaded usually get random numbers
    full_name = str(name) + ".png"
    #downloading the image
    urllib.request.urlretrieve(url, full_name, reporthook= None, data = None)

    


#image URL = https://she-codes.org/wp-content/uploads/2014/11/logo-copy200.png
#QA LINES
download_web_image('https://she-codes.org/wp-content/uploads/2014/11/logo-copy200.png')
