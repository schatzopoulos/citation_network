import luigi
import sys
import urllib2
from utils import mkdir, download, getVolumeFromUrl, getFilenameFromUrl
from bs4 import BeautifulSoup
from time import sleep

class Spider(luigi.Task):
	root_page = luigi.Parameter(default='http://dblp.uni-trier.de/db/journals/pvldb')
	download_dir = luigi.Parameter(default='/tmp/downloads/')

	def requires(self):
		return []

	# def output(self):
		# return luigi.LocalTarget(self.download_dir)

	# finds volume links from a root page of a dblp journal
	def findVolumeLinks(self, page):

		# get the html of the root page
		html = urllib2.urlopen(page)
		
		# parse the html code
		htmlTree = BeautifulSoup(html, 'html.parser')

		# links to journal volumes are inside ul elements
		uls = htmlTree.findAll('ul')

		links = []
		for ul in uls: 
			lis = ul.findAll('li')
			for li in lis: 
				if(li.text.startswith('Volume')): 
					href = li.find('a')['href']
					links.append(href)

		return links

	# finds paper pdf links from a dblp journal's volume page
	def findPdfPaperLinks(self, page): 

		# get the html of the root page
		html = urllib2.urlopen(page)
		
		# parse the html code
		htmlTree = BeautifulSoup(html, 'html.parser')

		pdfLinks = set()
		aTags = htmlTree.findAll('a')
		for tag in aTags: 
			href = tag['href']
			if(href.startswith('http://www.vldb.org') and href.endswith('pdf')):
				pdfLinks.add(href)

		return pdfLinks

	def run(self):

		# create the directory to download papers
		try: 
			mkdir(self.download_dir)
		except:
			print("#Error: Cannot create download directory") 
			sys.exit(-1)

		# find volume links in root page
		volumeLinks = self.findVolumeLinks(self.root_page)

		# follow volume links and parse each volume page
		for volumeLink in volumeLinks: 
			volumeName = getVolumeFromUrl(volumeLink)
			print "\nDownloading " + volumeName

			volumeDir = self.download_dir + volumeName
			mkdir(volumeDir)

			paperLinks = self.findPdfPaperLinks(volumeLink)
			for paperLink in paperLinks: 
				filename = getFilenameFromUrl(paperLink)
				path = volumeDir + '/' + filename
				print path
				download(paperLink, path)
				sleep(1)
				
			sleep(1)
