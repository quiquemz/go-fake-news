# Deprecated not needed


import pandas as pd
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features


def get_emotion(str):
    return data['emotion']['document']['emotion'][str]


def get_sentiment(val = False):
    if not val:
        return data['sentiment']['document']['label']
    else:
        return data['sentiment']['document']['score']


def get_entities():
    number_of_entities = len(data['entities'])
    i = 0
    string_to_add_to_csv = ""
    while i < number_of_entities:
        print(i)
        string_to_add_to_csv = "%s %s" % (string_to_add_to_csv, data['entities'][i]['text'])
        i += 1
    return string_to_add_to_csv


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
entities = []
sentiment = []

length_of_list = len(df['claim_course_url'])
print (length_of_list)

# response = natural_language_understanding.analyze(
#     url=df['claim_course_url'][0],
#     features=[features.Entities(limit=5), features.Emotion(), features.Sentiment()])


# print(response)
i = 0

while i < length_of_list:
    print(i)
    data = natural_language_understanding.analyze(
        url=df['claim_course_url'][0],
        features=[features.Entities(limit=5), features.Emotion(), features.Sentiment()])
    anger.append(get_emotion('anger'))
    joy.append(get_emotion('joy'))
    sadness.append(get_emotion('sadness'))
    fear.append(get_emotion('fear'))
    disgust.append(get_emotion('disgust'))
    entities.append(get_entities())
    sentiment.append(get_sentiment(True))
    i += 1
    if i == 900:
        username = raw_input("Enter Username: ")
        password = raw_input("Enter Password: ")
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2017-02-27',
            username=username,
            password=password)


df = df.assign(angerScore=anger)
df = df.assign(joyScore=joy)
df = df.assign(sadnessScore=sadness)
df = df.assign(disgustScore=disgust)
df = df.assign(fearScore=fear)
df = df.assign(sentimentScore=sentiment)
df = df.assign(entitiesScore=entities)



# df = df.assign(testnum=test)
df.to_csv('test.csv', index=False)
#print(len(df['claim_course_url']))
#print(df['claim_course_url'][0])
