from flask import Flask, url_for
from flask import request
from flask import Response
import WatsonAPI
import json
from flask import jsonify
# import script.py

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
        print(request.args['url'])
        data = WatsonAPI.emotion_analysis(request.args['url'])
        resp = jsonify(data)
        resp.headers.add("Access-Control-Allow-Origin", "*")
        resp.status_code = 200
        print (resp)
        return resp
    return 'Welcome'

    # data = {
    #     'hello': 'world',
    #     'number': 3
    # }
    # js = json.dumps(data)
    #
    # resp = Response(js, status=200, mimetype='application/json')
    # resp.headers.ad
    # resp.headers['Link'] = 'http://luisrei.com'
    #
    # return resp


@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')


@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == '__main__':
    app.run()
