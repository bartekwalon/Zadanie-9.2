import requests
import csv
import json

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

print(data[0]['rates'])

with open('ok.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, ['currency','code','bid','ask'])
    writer.writerows(data[0]['rates'])

from flask import Flask

app = Flask(__name__)

from flask import render_template
@app.route('/')
def converter():
    return render_template("Converter.htm")