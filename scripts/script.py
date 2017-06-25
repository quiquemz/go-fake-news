import pandas as pd
import numpy as np
import nltk
import sys
import newspaper
from newspaper import Article
# from newspaper import news_pool
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib

import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
def clean_content ( raw_article ):
    # Function to convert a raw article to a string of words
    # The input is a single string (a raw movie article), and 
    # the output is a single string (a preprocessed movie article)
    #
    # 1. Remove HTML
    article_text = BeautifulSoup(raw_article, "lxml").get_text() 
    #
    # 2. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", article_text) 
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()                             
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    # 
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    #
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( meaningful_words ))  

def learn():
	data = pd.read_csv("data.csv", encoding='utf-8')

	for idx, row in data.iterrows():
	    if(row["content"] is np.nan):
	        data.drop(idx, inplace=True)
	    elif(isinstance(row["content"], str)):
	        data.set_value(idx, "content", clean_content(row["content"]))

	X = data["label"].as_matrix()
	del data["label"]
	Y = data.as_matrix()

	X_train, X_test, y_train, y_test = train_test_split(
		 Y, X, test_size=0.33, random_state=42)

	count_vect = CountVectorizer()
	X_train_counts = count_vect.fit_transform(X_train[:,4])
	print(X_train_counts.shape)
	X_test_counts = count_vect.transform(X_test[:,4])
	print(X_test_counts.shape)
	tfidf_transformer = TfidfTransformer()
	X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
	X_test_tfidf = tfidf_transformer.transform(X_test_counts)
	print(X_train_tfidf.shape)
	print(X_test_tfidf.shape)

	# add punctuation features
	mnb_clf = MultinomialNB().fit(X_train_tfidf, y_train)
	ada_clf = AdaBoostClassifier(n_estimators=100).fit(X_train_tfidf, y_train)

	joblib.dump(mnb_clf, 'mnb_clf.pkl')
	joblib.dump(ada_clf, 'ada_clf.pkl')

	predicted = mnb_clf.predict(X_test_tfidf)
	ada_predictions = ada_clf.predict(X_test_tfidf)
	ada_score = np.mean(ada_predictions == y_test)
	mnb_score = np.mean(predicted == y_test)   

	print(mnb_score)
	print(ada_score)

def infer(url):
	"""
	Takes in a url string. It passes it through our classifiers to predict fake or real news.
	"""


	#######
	data = pd.read_csv("data.csv", encoding='utf-8')

	for idx, row in data.iterrows():
	    if(row["content"] is np.nan):
	        data.drop(idx, inplace=True)
	    elif(isinstance(row["content"], str)):
	        data.set_value(idx, "content", clean_content(row["content"]))

	X = data["label"].as_matrix()
	del data["label"]
	Y = data.as_matrix()

	X_train, X_test, y_train, y_test = train_test_split(
		 Y, X, test_size=0.33, random_state=42)

	count_vect = CountVectorizer()
	X_train_counts = count_vect.fit_transform(X_train[:,4])
	print(X_train_counts.shape)
	X_test_counts = count_vect.transform(X_test[:,4])
	print(X_test_counts.shape)
	tfidf_transformer = TfidfTransformer()
	X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
	X_test_tfidf = tfidf_transformer.transform(X_test_counts)
	#######
	a = Article(url)
	a.download()
	X = clean_content(a.html)#.reshape(1, -1)
	#print(X.shape) # shape is (1,1)	
	X_counts = count_vect.transform([X])

	print(X_counts.shape)
	X_tfidf = tfidf_transformer.transform(X_counts)
	print(X_tfidf.shape)

	mnb_clf = joblib.load('mnb_clf.pkl')
	ada_clf = joblib.load('ada_clf.pkl')
	
	mnb_score = mnb_clf.predict_proba(X_tfidf)	
	ada_score = ada_clf.predict_proba(X_tfidf)

	print("Adaboost score:")
	print(ada_score)
	print("mnb score:")
	print(mnb_score)

	return ada_score, mnb_score

def main():
	input_url = sys.argv[1]
	print(input_url)
	infer(input_url)

if __name__ == "__main__":
	main()
	# infer("http://www.theonion.com/article/scientists-confident-artificially-intelligent-mach-51170")

# infer("http://www.theonion.com/graphic/sean-spicer-cradling-comfort-pig-throughout-briefi-56317")
# learn()
