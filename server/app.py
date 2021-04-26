from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})
# setting up variables that will hold informations about the offers
offers = []

def pracujPlScraping(webpage, page_number):
     next_page = webpage + str(page_number)
     response= requests.get(str(next_page))
     result = BeautifulSoup(response.content, "html.parser")
     soup_title= result.findAll('div', class_='offer-details__text')
     soup_details= result.findAll('div', class_='offer-labels__wrapper')
     for x in range(len(soup_title)):
         offers.append({'Stanowisko': soup_title[x].text, 'Lokalizacja': soup_details[x].text})
         if page_number < 5:
             page_number = page_number + 1
             pracujPlScraping(webpage, page_number)

@app.route('/', methods=['GET'])
def getJob():
    return jsonify({"offers" : offers})

if __name__ == '__main__':
    pracujPlScraping('https://www.pracuj.pl/praca?pn=',1)
    app.run()
    