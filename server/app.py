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
     soup_title= result.findAll('a', class_='offer-details__title-link')
     soup_details= result.findAll('div', class_='offer-labels__wrapper')
     soup_links = result.findAll('a',class_='offer-details__title-link', href=True)
     soup_company = result.findAll('a', class_='offer-company__name')
     for x in range(len(soup_title)):
         offers.append({'Stanowisko': soup_title[x].text, 'Lokalizacja': soup_details[x].text, 'Link': soup_links[x]['href'], 'Pracodawca': soup_company[x].text})
         if page_number < 2:
             page_number = page_number + 1
             pracujPlScraping(webpage, page_number)

def pracaPlScraping(webpage1, page_number, webpage2):
    next_page = webpage1 + str(page_number) + webpage2
    response= requests.get(str(next_page))
    result = BeautifulSoup(response.content, "html.parser")
    soup_title=result.findAll('a', class_='listing__offer-title')
    soup_localization=result.findAll('div', class_='listing__location')
    soup_company=result.findAll('a', class_='listing__employer-name')
    soup_links=result.findAll('a', class_='listing__offer-title', href=True)
    for x in range (len(soup_title)):
        offers.append({'Stanowisko': soup_title[x].text, 'Lokalizacja': soup_localization[x].text, 'Link': 'https://www.praca.pl'+soup_links[x]['href'], 'Pracodawca': soup_company[x].text})
        if page_number < 2:
             page_number = page_number + 1
             pracaPlScraping(webpage1,page_number, webpage2)

def infopracaPlScraping(webpage, page_number):
    next_page = webpage + str(page_number)
    response= requests.get(str(next_page))
    result = BeautifulSoup(response.content, "html.parser")
    soup_title=result.findAll('a', class_='job-offer')
    soup_localization=result.findAll('span', class_='p-locality')
    soup_company=result.findAll('h3', class_='p-name company')
    soup_links=result.findAll('a', class_='job-offer', href=True)
    for x in range (len(soup_title)):
        offers.append({'Stanowisko': soup_title[x].text, 'Lokalizacja': soup_localization[x].text, 'Link': 'https://www.infopraca.pl'+soup_links[x]['href'] ,'Pracodawca': soup_company[x].text})
        if page_number < 2:
             page_number = page_number + 1
             infopracaPlScraping(webpage, page_number)

@app.route('/', methods=['GET'])
def getJob():
    return jsonify({"offers" : offers})

if __name__ == '__main__':
    pracujPlScraping('https://www.pracuj.pl/praca?pn=',1)
    pracaPlScraping('https://www.praca.pl/oferty-pracy_',1,'.html')
    infopracaPlScraping('https://www.infopraca.pl/praca?pg=',1)
    app.run()
    