import json

from flask import Flask
from datetime import datetime
from elasticsearch import Elasticsearch, helpers
import requests

app = Flask(__name__)


@app.route('/')
def hello_world() :
    # Password for the 'elastic' user generated by Elasticsearch
    ELASTIC_PASSWORD = "AZm5WW2-P*rjoASOJdmC"

    # Create the client instance
    client = Elasticsearch(
        "http://localhost:9200")

    # Successful response!
    print(client.info())
    return 'Hello World!'

@app.route('/test')
def test() :
    
    return 'test'


@app.route('/load',methods=['GET'])
def dataFromSQLtoES():
    es = Elasticsearch(
        "http://localhost:9200")
    data = requests.get("http://localhost:5001/load")
    matieres_dict = data.json()

    for i, matiere in enumerate(matieres_dict["matieres"]):
        print(matiere)
        resp = es.index(index="matiere", id=i,body=matiere)
        print(resp['result'])
    return "OK"



if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5000)
