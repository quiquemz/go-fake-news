import requests
import os
import json
import pandas as pd
import numpy as n
import time
import csv 
import newspaper
from newspaper import Article
from newspaper import news_pool
from newspaper import Source

# TODO add vaderSentiment
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib

# read csv
fname = "data.csv"
df_origin = pd.read_csv(fname, header=None)
data = df_origin.as_matrix()

print data.shape
# create list of Article objects
urls = data[1:,0].tolist()

# for each line in csv
articles = []
for i in range(len(urls)):
    # print "iteration:{} {} ".format(i,urls[i])
    articles.append(Article(url=urls[i]))

# create a source of aricltes
news_source = Source("https://www.dummyurl.com")
news_source.articles = articles
# create a news_pool for threading purposes
news_pool.set([news_source], threads_per_source=2)
news_pool.join() 

# iterate through article list to create a column for the csv
print "Parsing articles..."

article_list = []
labels = ['title','authors','text','keywords','summary','tags']
for article in articles:
		print "Parsing article {}".format(article.url)
		article.parse()
		article_list.append({ 
				labels[0]: article.title,
				labels[1]: article.authors,
				labels[2]: article.text,
				labels[3]: article.keywords,
				labels[4]: article.summary,
				labels[5]: article.tags
				}
			)

print "========================================="
print "Processed {} number of articles".format(len(article_list))


# create a pandas dataframe 
df = pd.DataFrame(article_list)

# append the new datafram to the original DataFramjeF
fname = 'new_data.csv'

df.to_csv(fname, encoding='utf-8')

