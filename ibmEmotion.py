import json
import pprint

from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='b4c673c4-124b-492b-badb-32a6bb20cbff',
    password='ZfIAKDLjp172')

response = natural_language_understanding.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
         'Superman fears not Banner, but Wayne.',
    features=[features.Entities(), features.Emotion(), features.Sentiment()])


print(response)
