from flask import Flask, url_for
from flask import request
import WatsonAPI
from flask import jsonify
import script, pprint
from pprint import pprint

app = Flask(__name__)


@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'


@app.route('/')
def api_root():
    if 'url' in request.args:
        # return 'Hello ' + request.args['url']
        data = WatsonAPI.emotion_analysis(request.args['url'])
        json_out = {}
        json_out['emotion'] = data
        credibility = script.run_code(request.args['url'])

        json_out['credibility'] = credibility[1]
        # pprint(json_out)

        # data.append(credibility)
        resp = jsonify(json_out)
        resp.headers.add("Access-Control-Allow-Origin", "*")
        resp.status_code = 200
        pprint(resp)
        return resp
    return 'Welcome'


@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run()
