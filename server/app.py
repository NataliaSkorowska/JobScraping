from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
from collections import Counter
import re
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['JSON_SORT_KEYS'] = False

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
         if page_number < 5:
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
        if page_number < 5:
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
        if page_number < 5:
             page_number = page_number + 1
             infopracaPlScraping(webpage, page_number)

miasta = []
def miastoScraping(webpage, page_number):
     next_page = webpage + str(page_number)
     response= requests.get(str(next_page))
     result = BeautifulSoup(response.content, "html.parser")
     soup_details= result.findAll('div', class_='offer-labels__wrapper')
     for x in range(len(soup_details)):
        if "lokalizacji" not in soup_details[x].text:
            miasta.extend({soup_details[x].text.strip()})
            if page_number < 7:
                page_number = page_number + 1
                miastoScraping(webpage, page_number)

umowy = [0,0,0,0,0]
etat = [0,0,0]
pozycja = [0,0,0,0,0]
def statScraping(webpage, page_number):
    next_page = webpage + str(page_number)
    response= requests.get(str(next_page))
    result = BeautifulSoup(response.content, "html.parser")
    dane = str(result.find('script', string=re.compile("typesOfContract")).string)
    skrypt = dane.split(',')
    umowaOPrace = 0
    for i in range(len(skrypt)):
        if 'Umowa o pracę' in skrypt[i]:
            umowaOPrace = umowaOPrace + 1
    umowy[0] = umowy[0] + umowaOPrace
    umowaZlecenie = 0
    for i in range(len(skrypt)):
        if 'Umowa zlecenie' in skrypt[i]:
            umowaZlecenie = umowaZlecenie + 1
    umowy[1] = umowy[1] + umowaZlecenie
    kontraktB2B = 0
    for i in range(len(skrypt)):
        if 'Kontrakt B2B' in skrypt[i]:
            kontraktB2B = kontraktB2B + 1
    umowy[2] = umowy[2] + kontraktB2B
    umowaAgencyjna = 0
    for i in range(len(skrypt)):
        if 'Umowa agencyjna' in skrypt[i]:
            umowaAgencyjna = umowaAgencyjna + 1
    umowy[3] = umowy[3] + umowaAgencyjna
    umowaStazPraktyki = 0
    for i in range(len(skrypt)):
        if 'Umowa o staż / praktyki' in skrypt[i]:
            umowaStazPraktyki = umowaStazPraktyki + 1
    umowy[4] = umowy[4] + umowaStazPraktyki
    pelnyEtat = 0
    for i in range(len(skrypt)):
        if 'Pełny etat' in skrypt[i]:
            pelnyEtat = pelnyEtat + 1
    etat[0] = etat[0] + pelnyEtat
    czescEtatu = 0
    for i in range(len(skrypt)):
        if 'Część etatu' in skrypt[i]:
            czescEtatu = czescEtatu + 1
    etat[1] = etat[1] + czescEtatu
    tymczasowa = 0
    for i in range(len(skrypt)):
        if 'Dodatkowa / tymczasowa' in skrypt[i]:
            tymczasowa = tymczasowa + 1
    etat[2] = etat[2] + tymczasowa
    menedzer = 0
    for i in range(len(skrypt)):
        if 'Menedżer' in skrypt[i]:
            menedzer = menedzer + 1
    pozycja[0] = pozycja[0] + menedzer
    specjalistaMidRegular = 0
    for i in range(len(skrypt)):
        if 'Specjalista (Mid / Regular)' in skrypt[i]:
            specjalistaMidRegular = specjalistaMidRegular + 1
    pozycja[1] = pozycja[1] + specjalistaMidRegular
    specjalistaSenior = 0
    for i in range(len(skrypt)):
        if 'Starszy specjalista (Senior)' in skrypt[i]:
            specjalistaSenior = specjalistaSenior + 1
    pozycja[2] = pozycja[2] + specjalistaSenior
    specjalistaJunior = 0
    for i in range(len(skrypt)):
        if 'Młodszy specjalista (Junior)' in skrypt[i]:
            specjalistaJunior = specjalistaJunior + 1
    pozycja[3] = pozycja[3] + specjalistaJunior
    fizyczny = 0
    for i in range(len(skrypt)):
        if 'Pracownik fizyczny' in skrypt[i]:
            fizyczny = fizyczny + 1
    pozycja[3] = pozycja[3] + fizyczny
    if page_number < 7:
        page_number = page_number + 1
        statScraping(webpage, page_number)

@app.route('/', methods=['GET'])
def getJob():
    return jsonify({"offers" : offers})

@app.route('/miasto', methods=['GET'])
def getMiasto():
    topten = Counter(miasta).most_common(10)
    city = []
    offer = []
    for x in topten:
        city.append(x[0])
        offer.append(x[1])
    return jsonify({
        city[0] : offer[0],
        city[1] : offer[1],
        city[2] : offer[2],
        city[3] : offer[3],
        city[4] : offer[4],
        city[5] : offer[5],
        city[6] : offer[6],
        city[7] : offer[7],
        city[8] : offer[8],
        city[9] : offer[9]})
        
@app.route('/umowa', methods=['GET'])
def getUmowa():
    return jsonify({
        'Umowa o pracę' : umowy[0],
        'Umowa zlecenie' : umowy[1],
        'Kontrakt B2B' : umowy[2],
        'Umowa agencyjna' : umowy[3],
        'Umowa o staż / praktyki' : umowy[4]
    })

@app.route('/etat', methods=['GET'])
def getEtat():
    return jsonify({
        'Pełny etat' : etat[0],
        'Część etatu' : etat[1],
        'Dodatkowa / tymczasowa' : etat[2]
    })

@app.route('/pozycja', methods=['GET'])
def getPozycja():
    return jsonify({
        'Menedżer' : pozycja[0],
        'Specjalista (Mid / Regular)' : pozycja[1],
        'Starszy specjalista (Senior)' : pozycja[2],
        'Młodszy specjalista (Junior)' : pozycja[3],
        'Pracownik fizyczny' : pozycja[4]
    })

if __name__ == '__main__':
    pracujPlScraping('https://www.pracuj.pl/praca?pn=',1)
    pracaPlScraping('https://www.praca.pl/oferty-pracy_',1,'.html')
    infopracaPlScraping('https://www.infopraca.pl/praca?pg=',1)
    miastoScraping('https://www.pracuj.pl/praca?pn=',1)
    statScraping('https://www.pracuj.pl/praca?pn=', 1)
    app.run()
    