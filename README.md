# go-fake-news
AI-Hachathon project 2

## To run: 
Clone the repository

### If you use virtualenv
In the directory of the cloned repository, create a virtualenv instance: `virtualenv venv` (on OSX)

Then activate it: `. venv/bin/activate`

### Install dependencies
Install [Flask](http://flask.pocoo.org/docs/0.12/installation/)

Install Polymer: `npm install -g polymer-cli`

Install modules: 
```
pip3 install --upgrade watson-developer-cloud
pip3 install pandas
pip3 install nltk
pip3 install sklearn
pip3 install scipy
pip3 install bs4
pip3 install keras
pip3 install tensorflow
pip3 install h5py
pip3 install newspaper3k
```
There may be more. Just pip3 install like above.

### Run dependencies
Change the directory to web-apps-2, then Start the polymer instance: 
```
cd web-apps-2
polymer serve --open
```

In a separate window, Start the Flask backend: `python3 server.py`

* if you use virtualenv, make sure you `. venv/bin/activate` in the new window
