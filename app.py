from flask import Flask, render_template, request

import pickle

#for data manipulations
import numpy as np
import pandas as pd
import cgi  
import requests
app = Flask(__name__)

soildata = pd.read_csv('soildata.csv')
from sklearn.cluster import KMeans

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route("/", methods=["GET"])
def home():
     return render_template('index.html')

@app.route('/form', methods=["GET"])
def form():
     print(request.form)
     return render_template('Form.html')


@app.route("/bajara", methods=["GET"])
def bajara():
     return render_template('Bajara.html')


@app.route("/jowar", methods=["GET"])
def jowar():
     return render_template('Jowar.html')


@app.route("/maize", methods=["GET"])
def maize():
     return render_template('Maize.html')

@app.route("/wheat", methods=["GET"])
def wheat():
     return render_template('WheatCrop.html')

@app.route("/rice", methods=["GET"])
def rice():
     return render_template('RiceCrop1.html')

@app.route('/process_form', methods=['POST'])
def getInput():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    city = request.form['tal'] 
    api_key = '2129dff76f701a1fdd061266ba34a79b' 
    params = {
        'q': city,
        'units': 'metric',
        'appid': api_key
    }
    # Send request to the API
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        hum = data['main']['humidity']
        rain = data.get('rain', {}).get('1h', 0)
    else:
        print(f"Failed to fetch weather data for {city}. Status code: {response.status_code}")

    filtered_df = soildata[soildata['Region'] == city]

    n = filtered_df.iloc[0]['N']
    p = filtered_df.iloc[0]['P']
    k = filtered_df.iloc[0]['K']

    ph = filtered_df.iloc[0]['ph']
    prediction = model.predict((np.array([[n, p, k, temp, hum, ph, rain]])))
    print(prediction)
    imageList = {}
    for i in prediction:
        if i == 'mango':
            imageList = {'Mango': '../static/images/mango.jpg'}
        if i=='rice':
          imageList={'Rice':'../static/images/rice.jpg'}
        if i=='pomegranate':
          imageList={'Pomegranate':'../static/images/pomegranate.jpg'}
        if i=='pigeonpeas':
          imageList={'Pigeonpeas':'../static/images/pigeonpeas.jpeg'}
        if i=='papaya':
          imageList={'Papaya':'../static/images/papaya.jpg'}
        if i=='orange':
          imageList={'Orange':'../static/images/orange.jpg'}
        if i=='muskmelon':
          imageList={'Muskmelon':'../static/images/muskmelon.jpeg'}
        if i=='mungbean':
          imageList={'Mungbean':'../static/images/mungbeans.jpg'}
        if i=='mothbeans':
          imageList={'Mothbean':'../static/images/mothbean.jpeg'}
        if i=='lentil':
          imageList={'Letil':'../static/images/lentil.jpg'}
        if i=='kidneybeans':
          imageList={'Kidneybeans':'../static/images/kidneybean.jpeg'}
        if i=='grapes':
          imageList={'Grapes':'../static/images/grapes.jpeg'}
        if i=='jute':
          imageList={'Jute':'../static/images/jute.jpg'}
        if i=='blackgram':
          imageList={'Blackgram':'../static/images/blackgram.jpg'}
        if i=='apple':
          imageList={'Apple':'../static/images/apple2.jpeg'}
        if i=='coffee':
          imageList={'Coffee':'../static/images/coffee.jpeg'}
        if i=='maize':
          imageList={'Maize':'../static/images/maize.png'}
        if i=='watermelon':
          imageList={'Watermelon':'../static/images/watermelon.jpeg'}
        if i=='banana':
          imageList={'Banana':'../static/images/banana.jpeg'}
        if i=='coconut':
          imageList={'Coconut':'../static/images/coconut.jpg'}
        if i=='cotton':
          imageList={'Cotton':'../static/images/cotton.jpeg'}
        
    return render_template('Form.html', res=imageList)
