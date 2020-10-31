# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:39:02 2020

@author: Chait
"""
#author chaitaya
#voice recognised shortst root
import speech_recognition as sr
import os

from kivy.app import App

import pyttsx3

from time import strftime
engine = pyttsx3.init('sapi5') 
import numpy as np
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 
def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
def kdo():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("wHAT IS STARTING POINT")
        print('wHAT IS STARTING POINT')
        
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        speak('You said: ' + command + '\n')
        print('You said: ' + command + '\n')
    except sr.UnknownValueError:
        print('....')
    with sr.Microphone() as source:
        speak("wHAT IS ENDING POINT")
        print('wHAT IS ENDING POINT')
     
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command1 = r.recognize_google(audio).lower()
        speak('You said: ' + command1 + '\n')
        print('You said: ' + command1 + '\n')
    except sr.UnknownValueError:
        print('....')
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(command)
    location1 = geolocator.geocode(command1)
    from geopy.distance import great_circle 


    kolkata = (location.latitude, location.longitude)
    delhi = (location1.latitude, location1.longitude) 
    speak('shortest distance is')

    speak(great_circle(kolkata, delhi).km )
    speak('kilometers')
    print(great_circle(kolkata, delhi).km) 
    p=0
    p=[location.latitude, location.longitude,location1.latitude, location1.longitude]
    return p
def sofiaResponse(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)
import webbrowser
def juy():
    import gmplot
    a=0
    p=kdo()
    lat=[p[0],p[2]]
    lon=[p[1],p[3]]
    gmo=gmplot.GoogleMapPlotter(p[0],p[1],11)
    gmo.scatter(lat,lon,size=50,marker=False)
    gmo.plot(lat,lon,'blue',edge_width=2.5)
    gmo.draw('map.html')
    gr(a)
def gr(instance):
     webbrowser.open('map.html')
    
from kivy.uix.image import Image
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout 
from kivy_garden.mapview import MapView
from kivy_garden.mapview  import MapMarkerPopup
from kivy_garden.mapview import MapMarker
class SimpleApp(App):
    def build(self):
        
        s=BoxLayout(orientation ='vertical') 
        
        def a(instance,value):
            print("welcome to edureka")
        btn = Button(text ="GO", font_size=150,
                     background_normal = r'C:\Users\Chait\Pictures\l.jpg', 
                     background_down = r'C:\Users\Chait\Pictures\l.jpg', 
                     size_hint = (1, 1), 
                       )
        btn.bind(on_press=lambda x:juy())
        
        s.add_widget(btn)
        
        
        return s
 
if __name__ == "__main__":
    SimpleApp().run()
     