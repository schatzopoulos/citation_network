import os
import errno
import urllib

def mkdir(path):
	try:
		os.makedirs(path)
	except OSError as exception:
	    if exception.errno != errno.EEXIST:
	        raise

def download(url, filename):
	urllib.urlretrieve(url, filename)

def getVolumeFromUrl(url): 
	lastSlash = url.rfind('/')
	lastDot = url.rfind('.')
	return url[lastSlash+1:lastDot]

def getFilenameFromUrl(url):
	lastOccur = url.rfind('/')
	return url[lastOccur+1:]