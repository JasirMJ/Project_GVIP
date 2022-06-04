#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import requests
import speech_recognition as sr
from time import ctime
import time
import cv2
import numpy as np
import pyttsx3

# # importing geopy library
# from geopy.geocoders import Nominatim
#
# # calling the Nominatim tool
# loc = Nominatim(user_agent="GetLoc")
#
# # entering the location name
# getLoc = loc.geocode("Gosainganj Lucknow")
#
# # printing address
# print(getLoc.address)
#
# # printing latitude and longitude
# print("Latitude = ", getLoc.latitude, "\n")
# print("Longitude = ", getLoc.longitude)

def speak(audioString):
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()

def get_output_layers(net):
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    color = COLORS[class_id]
    cv2.rectangle(img, (x, y), (x_plus_w, y_plus_h), color, 2)
    cv2.putText(img, label, (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

def recordAudio():
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=1)
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say " + MyText)
            return  MyText

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return  "Not clear"
    except sr.UnknownValueError:
        print("unknown error occured")
        return "Unknown error occured"


def jarvis(data):

    if "check" in data:
        message = "what you want to check"
        print("GVIP : ",message)
        speak(message)

    if "hello" in data:
        message = "yes i am listening"
        print("GVIP : ", message)
        speak(message)

    if "name" in data:
        message = "My name is jasi version 1.0 developed as a prototype"
        print("GVIP : ", message)
        speak(message)

    if "say something" in data:
        message = "One day i will become something"
        print("GVIP : ", message)
        speak(message)

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


# initialization
time.sleep(2)
speak("Hi Jasir, what can I do for you?")

detect = False
exit=False

config_path = 'yolov3.cfg'
weights_path = 'yolov3.weights'
classes_path = 'yolov3.txt'

dangerous_objects = ['person', 'car', 'motorcycle', 'bus', 'train', 'truck', 'bear', 'zebra', ]

video = cv2.VideoCapture(0)
# Initialize the recognizer
r = sr.Recognizer()

while 1:
    data = recordAudio()

    if detect:
        hasFrame, image = video.read()
        Width = image.shape[1]
        Height = image.shape[0]
        scale = 0.00392
        classes = None
        with open(classes_path, 'r') as f:
            classes = [line.strip() for line in f.readlines()]

        COLORS = np.random.uniform(0, 255, size=(len(classes), 3))
        net = cv2.dnn.readNet(weights_path, config_path)
        blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(get_output_layers(net))
        class_ids = []
        confidences = []
        boxes = []
        conf_threshold = 0.5
        nms_threshold = 0.4

        for out in outs:
            # print("Out ",out)
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                # print("Class ID : ", class_id, "Confidence : ", confidence)
                if confidence > 0.5:
                    center_x = int(detection[0] * Width)
                    center_y = int(detection[1] * Height)
                    w = int(detection[2] * Width)
                    h = int(detection[3] * Height)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

        for i in indices:
            i = i
            box = boxes[i]
            x = box[0]
            y = box[1]
            w = box[2]
            h = box[3]
            draw_prediction(image, class_ids[i], confidences[i], round(x), round(y), round(x + w), round(y + h))
            objectname = str(classes[class_ids[i]])
            print("Class ID : ", objectname, "Confidence : ", confidences[i])
            if objectname in dangerous_objects and confidences[i] > 0.9:
                msg = "Alert, Dangerous object detected " + objectname
                print(msg)
                speak(msg)


    if data=="open eyes":
        detect = True
        speak("Im opening my eyes for you")
        print("Im opening my eyes for you")

    elif data == "close eyes":
        detect = False
        speak("Detection is stopped")
        print("Detection is stopped")
        video.release() #close cam

    else: exit = jarvis(data)

    print("Exit ? ",exit)
    if exit:
        break
