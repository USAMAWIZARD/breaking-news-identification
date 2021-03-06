import feedparser
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
mostrep={}
tokenizer = RegexpTokenizer(r'\w+')
titleofallnews=[]
stop_words = set(stopwords.words('english')) 
aljazeera = feedparser.parse("http://america.aljazeera.com/content/ajam/articles.rss")
bbc=feedparser.parse("http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml")
cnn=feedparser.parse("http://rss.cnn.com/rss/cnn_education.rss")
cnbcworld=feedparser.parse("https://www.cnbc.com/id/100727362/device/rss/rss.html")
cnbctop= feedparser.parse("https://www.cnbc.com/id/100003114/device/rss/rss.html")
  
def mostcommonwordnews():
	global titleofallnews
	for newsheadline in titleofallnews:
		for word in newsheadline:
			mostrep[word.lower()]+=1
			

	print({k: v for k, v in sorted(mostrep.items(), key=lambda item: item[1])})
for news in aljazeera.entries+bbc.entries+cnn.entries+cnbcworld.entries+cnbctop.entries	:

	wordtokenized=word_tokenize(news.title)
	stop_word_removed_sentence = [w for w in wordtokenized if not w in stop_words]
	sentence_without_puct=tokenizer.tokenize(str(stop_word_removed_sentence)  )
	for word in sentence_without_puct:
		mostrep[word.lower()]=0
	titleofallnews.append(sentence_without_puct)
mostcommonwordnews()
#print(titleofallnews)
