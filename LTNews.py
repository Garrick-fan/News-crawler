from ArticleCrawler import ArticleCrawler 
from Article import Article
class LTNews(ArticleCrawler):
  def __init__(self, url):
    super(LTNews,self).__init__(url)
    self.url = url
    self.Articles = []
    self.urlArgv = ""
    self.maxUrlListID = ""

    self.init()

  def init(self):
    self.urlArgv, self.maxUrlListID = self.getMaxPageUrl()

  def getTitle(self):
    return self.soup.find('h2', class_='title').get_text().strip()

  def getContent(self):
    p_list = self.soup.find('div', class_='content').find_all('p')
    name=["En", "Ch"] 
    isDictionary = False
    title  = self.getTitle()
    author = p_list[0].get_text().strip()
    cnt = 0
    article = Article(title, author)
    paragraph = ["", ""]
    for p in range(1, len(p_list)):
      content = p_list[p].get_text().strip()
      if(content == ""):
        continue;
      elif(content == u"\u65b0\u805e\u8fad\u5178"):
        isDictionary = True
        continue
      elif(isDictionary):
        article.addDictionary(content)
      else:
        paragraph[cnt%2] = content
        if(cnt%2):
          article.addParagraph(paragraph[0], paragraph[1])
        cnt = cnt + 1
    self.Articles.append(article)
    print(article)

  def getMaxPageUrl(self):
    return self.soup.find('a', class_='p_last')['href'].split("=")

  def getNewsUrls(self, url):
    self.initRequest(url)
    a_list = self.soup.find('table', class_='table_english').find_all('a')
    urls = []
    for a in a_list:
      title = a.get_text() 
      href  = a['href']
      urls.append(self.url+href)
    return urls
  
  def GetArticlesWithUrlListID(self, listID):
    urlPage = self.url+self.urlArgv+"="+str(listID)
    urlNews = self.getNewsUrls(urlPage)
    for url in urlNews:
      self.initRequest(url)
      self.getContent()

  def GetAllArticles(self):
    for i in range(1, int(self.maxUrlListID)+1):
      self.GetArticlesWithUrlListID(i)
