import pandas as pd
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='b4c673c4-124b-492b-badb-32a6bb20cbff',
    password='ZfIAKDLjp172')

df = pd.read_csv('emergent.csv', sep=',', header=0)
dicts = df.to_dict()
anger = []
joy = []
sadness = []
fear = []
disgust = []


response = natural_language_understanding.analyze(
    url = df['claim_course_url'][0],
    features=[features.Entities(limit = 5), features.Emotion(), features.Sentiment()])


print(response)



# df = df.assign(testnum=test)
# df.to_csv('test.csv', index=False)
#print(len(df['claim_course_url']))
#print(df['claim_course_url'][0])
