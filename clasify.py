import feedparser
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
titleofallnews=[]
stop_words = set(stopwords.words('english')) 
aljazeera = feedparser.parse("http://america.aljazeera.com/content/ajam/articles.rss")
bbc=feedparser.parse("http://feeds.bbci.co.uk/news/world/us_and_canada/rss.xml")
cnn=feedparser.parse("http://rss.cnn.com/rss/cnn_education.rss")
cnbcworld=feedparser.parse("https://www.cnbc.com/id/100727362/device/rss/rss.html")
cnbctop= feedparser.parse("https://www.cnbc.com/id/100003114/device/rss/rss.html")
  

  
for news in aljazeera.entries+bbc.entries+cnn.entries+cnbcworld.entries+cnbctop.entries	:

	wordtokenized=word_tokenize(news.title)
	stop_word_removed_sentence = [w for w in wordtokenized if not w in stop_words]
	sentence_without_puct=tokenizer.tokenize(stop_word_removed_sentence)  
	titleofallnews.append(stop_word_removed_sentence)

print(titleofallnews)
