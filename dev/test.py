import json, pprint
from pprint import pprint
data = {'emotion': {'document': {'emotion': {'anger': 0.106514, 'joy': 0.624548,
'sadness': 0.482753, 'fear': 0.442205, 'disgust': 0.508437}}}, 'entities':
[{'relevance': 0.928023, 'text': 'DC Toys Collector', 'type': 'Company',
'count': 14}, {'relevance': 0.913179, 'text': 'Daiane DeJesus', 'type':
'Person', 'count': 18}, {'relevance': 0.854009, 'text': 'LA',
'disambiguation': {'subtype': ['GovernmentalJurisdiction',
'OlympicBiddingCity', 'OlympicHostCity', 'PlaceWithNeighborhoods',
'FilmScreeningVenue', 'City'], 'name': 'Los Angeles', 'dbpedia_resource':
'http://dbpedia.org/resource/Los_Angeles'}, 'type': 'Location', 'count':
11}, {'relevance': 0.767429, 'text': 'Messias Credido', 'type': 'Person',
'count': 12}, {'relevance': 0.70499, 'text': 'NYC', 'disambiguation':
{'subtype': ['City']}, 'type': 'Location', 'count': 7}], 'language':
'en', 'sentiment': {'document': {'score': 0.233746, 'label': 'positive'}},
'retrieved_url':
'http://www.dailymail.co.uk/news/article-2958242/Brazilian-former-porn-star-Diane-DeJesus-mystery-figure-5million-year-YouTube-sensation-DC-Toys-Collector.html'}


print(data)
print("newLine")
print("newLine")
print("newLine")
print("newLine")

# pprint(data['emotion']['document']['emotion'])


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


# pprint(get_entities())
# print(get_emotion('anger'))
# print(get_sentiment())
