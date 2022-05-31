from xmlrpc.client import ResponseError
from django.shortcuts import render
import pyttsx3
import requests
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from datetime import datetime

# Create your views here.
import threading

class SpeakView(ListAPIView):
    def get(self,request):
        message = self.request.GET.get('message',"")
        print(message)
        speak(message)
        return JsonResponse({'status':1,'message':'success'})

API_KEY = "cc02eecfa892c5ad1a78c3e49bbc3a8a"

def get_date(request):
    x_date = datetime.now().strftime("%A,%d %B, %Y")
    msg = f"Current Date is {x_date}"
    speak(msg)
    return JsonResponse({"message":msg, "status":1})

def get_time(request):
    x_time = datetime.now().strftime("%I:%M %p")
    msg = f"Current time is {x_time}"
    speak(msg)
    return JsonResponse({"message":msg, "status":1})

def get_weather(request):

    lat = "76.9366"
    lon = "8.5241"



    lat = "76.2254"
    lon = "10.976"



     


    API = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    res = requests.get(API).json()
    
    main = res['weather'][0]['main']
    description = res['weather'][0]['description']

    msg = f"The weather is {main} and it is {description}"

    speak(msg)
    return JsonResponse({"message":msg, "status":1,"data":res})

def speak(audioString):
    print("spekaing " ,audioString)
    #


    engine = pyttsx3.init()

    if engine._inLoop:
        print("Engine loop ",engine._inLoop)
        engine.endLoop()
        print("engine loop stopped")
        print("Engine loop ",engine._inLoop)


    # rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    voice = engine.getProperty('voice')
    #
    # engine.setProperty('rate', rate - 70)
    # rate = engine.getProperty('rate')
    # volume = engine.getProperty('volume')
    # voices = engine.getProperty('voices')
    # # engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    #
    engine.say(audioString)
    engine.runAndWait()

    # engine = pyttsx3.init()
    # engine.say(audioString)
    # engine.startLoop(False)
    # # engine.iterate() must be called inside Server_Up.start()
    # Server_Up = threading.Thread(target=Comm_Connection)
    # Server_Up.start()
    # engine.endLoop()


    #
    # print(audioString)
    # # tts = gTTS(text=audioString, lang='en')
    #
    # engine = pyttsx3.init()
    # engine.say(audioString)
    # engine.runAndWait()

    print("Audio message worked")
