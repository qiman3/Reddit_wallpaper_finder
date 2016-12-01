#!/usr/bin/env python3

import ctypes
import praw
import time
import urllib.request
import os
from itertools import cycle

USERAGENT = "/u/qiman3's Wallpaper finder"
SUBREDDIT = "ImaginaryBestOf"
IMAGEFOLDERPATH = "C:/Users/adam/Documents/Python_Scripts/Wallpaper_Test/"
MAXPOSTS= 100
TIMEBETWEENIMAGES = 30
SPI_SETDESKWALLPAPER = 20
FILETYPES = ('.jpg', '.jpeg', '.png')

def download_images(url_list):
	for idx, url in url_list:
		ext = os.path.splitext(url)[1]
		local_name = "{:0>4}{}".format(idx, ext)
		local_path = os.path.join(IMAGEFOLDERPATH, local_name)
		urllib.request.urlretrieve(sURL,local_path)

def findImages():
	print("LOGGING IN!")
	r = praw.Reddit(USERAGENT)
	print("LOGGED IN!")
	sReddit = r.get_subreddit(SUBREDDIT)
	urls = []
	for submision in sReddit.get_hot(Limit=None):
		sURL = submision.url
		sURL = sURL.rsplit("?", 1)[0]
		sTitle = submision.title
		if sURL.lower().endswith(FILETYPES):
			urls.append(sURL)
	return urls

def list_images():
	for file in os.listdir(IMAGEFOLDERPATH):
		if file.endswith(FILETYPES):
			yield os.path.join(IMAGEFOLDERPATH, file)

def cycleImages():
	'''this function can be run anytime to cycle images currently in IMAGEFOLDERPATH'''
	for imagePath in cycle(list_images()):
		ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagePath , 0)
		time.sleep(TIMEBETWEENIMAGES)

def removeFiles():
	for file in list_images():
		os.remove(file)

def main():
	removeFiles()
	download_images(findImages())
	cycleImages()

if __name__ == '__main__':
	main()
