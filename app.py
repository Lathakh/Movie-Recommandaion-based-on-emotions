# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:59:33 2021

@author: Admin
"""

from flask import Flask, request, render_template
import numpy as np
import re
import requests as HTTP
from bs4 import BeautifulSoup as SOUP
app = Flask(__name__)
app=Flask(__name__,template_folder="templates") 


@app.route('/',methods=['GET'])
def index():
    return render_template('home.html')

@app.route('/home', methods=['GET'])
def about():
    return render_template('home.html')

@app.route('/predict', methods=["GET","POST"])
def predict():
    #emotion=None
    #urlhere='http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
    if request.method == "POST":
        emotion=request.form['emotion']
    print(emotion)
    if(emotion == "happy"):
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "angry"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "disgust"):
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "think"):
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "sad"):
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
    response = HTTP.get(urlhere)
    data = response.text
    soup = SOUP(data, "lxml")
    supa = soup.find_all('h3', attrs={'class' : 'lister-item-header'})
    list = []
    for header in supa:
        name = "";   
        aElement_soup = header.find_all('a')
        spanElement_soup = header.find_all('span')
        spanElement = spanElement_soup[0]
        name = name + spanElement.text
        aElement = aElement_soup[0]
        name = name + "" + aElement.text
        if len(spanElement_soup)>1:
            spanElement = spanElement_soup[1]
            name = name + "\n" + spanElement.text
        list.append(name)
    
    return render_template('home.html',prediction_text="{}".format(emotion),data=list)

if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)
    
#localhost:5000
    
