from Paragraph import Paragraph 
class Article(object):
	def __init__(self, title = "", author = ""):
		self.title = title
		self.author = author
		self.paragraphs = []
		self.dictionary = []

	def addParagraph(self, enParagraph, chParagraph):
		paragraph = Paragraph(enParagraph, chParagraph)
		self.paragraphs.append(paragraph)

	def addDictionary(self, dictionary):
		self.dictionary.append(dictionary)

	def __str__(self):  
		description  = "title"  + self.title  + "\n"
		description += "author" + self.author + "\n"
		for i in self.paragraphs:
  			description += i.__str__() + '\n'
		for i in self.dictionary:
  			description += "[D]" + i + "\n"
		return description