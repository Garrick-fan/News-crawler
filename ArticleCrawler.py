import requests
from bs4 import BeautifulSoup 
from Article import Article

class ArticleCrawler:
	def __init__(self, url):
		self.soup = []
		self.initRequest(url)
		self.Articles = []
	def initRequest(self, url):
		start_html = requests.get(url)
		self.soup  = BeautifulSoup(start_html.text, 'lxml')
	def getContent():
		pass
	def getTitle():
		pass