from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
# from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})



# sanity check route
@app.route('/', methods=['GET'])
def getJob():
    return jsonify({
            'status': 'success',
            'job_titles': job_titles
    })


if __name__ == '__main__':
    job_titles=[]
    #retrieve the HTML data
    URL = 'https://www.pracuj.pl/praca'
    page = requests.get(URL)    

    results = BeautifulSoup(page.content, 'html.parser')
    job_elems = results.find_all('a', class_='offer-details__title-link')
    for job_elem in job_elems:
        job_titles.append(job_elem.text)
        print(job_elem.text, end='\n'*2)

    app.run()
    