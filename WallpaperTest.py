import ctypes
import praw
import time
import urllib.request
import os

USERAGENT = "/u/qiman3's Wallpaper finder"
SUBREDDIT = "ImaginaryBestOf"
IMAGEFOLDERPATH = "C:/Users/adam/Documents/Python_Scripts/Wallpaper_Test/"
MAXPOSTS= 100
TIMEBETWEENIMAGES = 30
print("LOGGING IN!")
r = praw.Reddit(USERAGENT)
print("LOGGED IN!")

def findImages():
	sReddit = r.get_subreddit(SUBREDDIT)
	i = 0
	for submision in sReddit.get_hot(Limit=None):
		sURL = submision.url
		sTitle = submision.title
		if "jpg" in sURL:
			print("{} {}".format(i,sTitle))
			urllib.request.urlretrieve(sURL, "{}/{}.jpg".format(IMAGEFOLDERPATH,i))
			i = i+1
	return i
def cycleImages(numberofImages):
	i = 0
	while True:
		imagePath = ("{}/{}.jpg".format(IMAGEFOLDERPATH,i))
		SPI_SETDESKWALLPAPER = 20 
		ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagePath , 0)
		i = (i + 1) % numberofImages
		time.sleep(TIMEBETWEENIMAGES)
def removeFiles():
	for file in os.listdir(IMAGEFOLDERPATH):
		if file.endswith(".jpg"):
			os.remove(file)
def main():
	removeFiles()
	cycleImages(findImages())
main()