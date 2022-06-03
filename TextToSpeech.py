#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import requests
import speech_recognition as sr
from time import ctime
import time
import os
# from gtts import gTTS
import pyttsx3

# importing geopy library
from geopy.geocoders import Nominatim

# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

# entering the location name
getLoc = loc.geocode("Gosainganj Lucknow")

# printing address
# print(getLoc.address)
#
# # printing latitude and longitude
# print("Latitude = ", getLoc.latitude, "\n")
# print("Longitude = ", getLoc.longitude)


def speak(audioString):
    print(audioString)
    # tts = gTTS(text=audioString, lang='en')

    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()

    # tts.save("audio.mp3")
    # os.system("pip audio.mp3")

def xrecordAudio():
    # Record Audio
    r = sr.Recognizer()
    r.energy_threshold = 300
    with sr.Microphone() as source:
        print("Say something!")
        # print("source ",source)
        audio = r.listen(source)
        print("audio ",audio)

        # if not audio:
        #     print("Say ")

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        speak("i did not understand")
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data

# Initialize the recognizer
r = sr.Recognizer()

def recordAudio():
    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say " + MyText)
            # SpeakText(MyText)
            return  MyText

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return  "Not clear"
    except Exception as e:
        print("unknown error occured ",e)
        return 0
    # except sr.UnknownValueError:
    #     print("unknown error occured ",sr.UnknownValueError)
    #     return 0


def jarvis(data):

    if "check" in data:
        message = "what you want to check"
        print("GVIP : ",message)
        speak(message)

    if "hello" in data:
        message = "yes i am listening"
        print("GVIP : ", message)
        speak(message)

    if "name"  in data:
        message = "My name is jasi version 1.0 developed as a prototype"
        print("GVIP : ", message)
        speak(message)

    if "say something" in data:
        message = "One day i will become something"
        print("GVIP : ", message)
        speak(message)

    if "tell me a joke" in data:

        url = "https://v2.jokeapi.dev/joke/Any"
        res = requests.get(url)
        res = res.json()
        qs = res['setup']
        ans = res['delivery']
        print(qs)
        print(ans)
        speak("here is the question.")
        speak(qs)
        time.sleep(1)

        speak("Here is the answer.")
        speak(ans)




    if "what is your name" in data:
        message = "My name is Gvip version 1.0 developed as a prototype"
        print("GVIP : ", message)
        speak(message)

    if "who created you" in data:
        message = "Mohamed jasir created me"
        print("GVIP : ", message)
        speak(message)

    if "you work for" in data:
        message = "Jasir"
        print("GVIP : ", message)
        speak(message)

    if "what is your aim" in data:
        message = "my aim is to build a better tomorrow"
        print("GVIP : ", message)
        speak(message)

    if "how are you" in data:
        message = "I am fine"
        print("GVIP : ", message)
        speak(message)

    if "bye" in data:
        message = "ok see ya"
        print("GVIP : ", message)
        speak(message)
        return True

    if "see ya" in data:
        message = "ok see ya"
        print("GVIP : ", message)
        speak(message)
        return True

    if "what time is it" in data:
        speak(ctime())

    if "where is " in data:
        data = data.split(" ")
        location = data[2]
        print("Location :",location)
        speak(location+ ' is some where on the earth')
        # speak("Hold on Frank, I will show you where " + location + " is.")
        # os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
        # os.system("chrome https://www.google.nl/maps/place/" + location + "/&amp;")
    return False

# initialization
time.sleep(2)
speak("Hi Jasir, what can I do for you?")





#
while 1:
    data = recordAudio()
    if data:
        exit = jarvis(data)
    else:
        print("Skipped")

    print("exit ? ",exit)
    if exit:
        break
