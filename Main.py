import Config	
import sys
from LTNews import LTNews 

URL_HOME = Config.URL_HOME
if(len(sys.argv) == 1):
	print("argv error: python Main.py 'URLID'")
	exit(0)

URL_LIST_ID = sys.argv[1]

LTN = LTNews(URL_HOME)
LTN.GetArticlesWithUrlListID(URL_LIST_ID)

