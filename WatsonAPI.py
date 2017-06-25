# import pandas as pd
# import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features




# def get_sentiment(val=False):
#     if not val:
#         return data['sentiment']['document']['label']
#     else:
#         return data['sentiment']['document']['score']


# def get_entities():
#     number_of_entities = len(data['entities'])
#     i = 0
#     string_to_add_to_csv = ""
#     while i < number_of_entities:
#         print(i)
#         string_to_add_to_csv = "%s %s" % (string_to_add_to_csv, data['entities'][i]['text'])
#         i += 1
#     return string_to_add_to_csv


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='4466e42c-ace7-483d-af17-31d80246f9b1',
    password='BYoIDLNYeCQG')

# df = pd.read_csv('emergent.csv', sep=',', header=0)
# dicts = df.to_dict()
# anger = []
# joy = []
# sadness = []
# fear = []
# disgust = []
# entities = []
# sentiment = []


def emotion_analysis(link):

    data = natural_language_understanding.analyze(
        url=link,
        features=[features.Emotion()])

    def get_emotion(emo):
        return data['emotion']['document']['emotion'][emo]

    emotion = []

    # length_of_list = len(df['claim_course_url'])
    # print (length_of_list)

    print(data)
    # i = 0

    # print(i)

    emotion.append(get_emotion('anger'))
    emotion.append(get_emotion('sadness'))
    emotion.append(get_emotion('disgust'))
    emotion.append(get_emotion('fear'))
    emotion.append(get_emotion('joy'))
    return emotion

# entities.append(get_entities())
# sentiment.append(get_sentiment(True))
# i += 1
# Incase API runs out
# if i == 900:
#     username = raw_input("Enter Username: ")
#     password = raw_input("Enter Password: ")
#     natural_language_understanding = NaturalLanguageUnderstandingV1(
#         version='2017-02-27',
#         username=username,
#         password=password)


# df = df.assign(angerScore=anger)
# df = df.assign(joyScore=joy)
# df = df.assign(sadnessScore=sadness)
# df = df.assign(disgustScore=disgust)
# df = df.assign(fearScore=fear)
# df = df.assign(sentimentScore=sentiment)
# df = df.assign(entitiesScore=entities)



# df = df.assign(testnum=test)
# df.to_csv('test.csv', index=False)
#print(len(df['claim_course_url']))
#print(df['claim_course_url'][0])
