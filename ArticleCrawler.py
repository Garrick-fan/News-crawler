import requests
from bs4 import BeautifulSoup 
from Article import Article 
class ArticleCrawler:
	def __init__(self, url):
		self.soup = []
		self.request = []
		self.Articles = []
		self.initRequest(url)
	def initRequest(self, url):
		self.request = requests.get(url)
		self.soup = BeautifulSoup(self.request.text, 'lxml')
	def getContent():
		pass
	def getTitle():
		pass