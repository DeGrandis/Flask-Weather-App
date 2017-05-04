from flask import Flask, render_template
import requests
import time

locationURL = "http://ipinfo.io/"

location = requests.get(locationURL)
location = location.json()
zipCode = location['postal']

weatherURL = "http://api.openweathermap.org/data/2.5/weather?zip=" + zipCode + ",us&APPID=224cda3d36240ea7aa8e98b855204d8c"


    

app = Flask(__name__)

@app.route("/")
def index():
    r = requests.get(weatherURL)
    data = r.json()
    K = int(data['main']['temp'])
    temperature =  (1.8) * (K - 273) + 32
    
    return render_template('index.html', temperature=temperature, location=location)

@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == "__main__":
    app.run(debug = True)