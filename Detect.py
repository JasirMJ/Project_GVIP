#############################################
# Object detection - YOLO - OpenCV
# Author : Arun Ponnusamy   (July 16, 2018)
# Website : http://www.arunponnusamy.com
############################################


import cv2
import argparse
import numpy as np
import pyttsx3

import requests
from os import system

config_path = 'yolov3.cfg'
weights_path ='yolov3.weights'
classes_path =  'yolov3.txt'

dangerous_objects = ['person','car','motorcycle','bus','train','truck','bear','zebra',]

ap = argparse.ArgumentParser()
# ap.add_argument('-i', '--image', required=True,
#                 help = 'path to input image')
# ap.add_argument('-c', '--config', required=True,
#                 help = 'path to yolo config file')
# ap.add_argument('-w', '--weights', required=True,
#                 help = 'path to yolo pre-trained weights')
# ap.add_argument('-cl', '--classes', required=True,
#                 help = 'path to text file containing class names')
args = ap.parse_args()

video=cv2.VideoCapture(0)
# print("Arguments readed")

def get_output_layers(net):
    # print("Getting output layers called")
    layer_names = net.getLayerNames()
    # print("Layer names len: ", len(layer_names))
    # print("net layer len",len(net.getUnconnectedOutLayers()))

    # for i in net.getUnconnectedOutLayers():

    #     # print("i is ",i)
    #     # print("i is ",type(i))
    #     # print("i is ",i[0] - 1)
    #     print("i is ",i[0])
        
    
    # output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    # output_layers = [layer_names[i - 1] for i in range(1,10)]
    # print("Output layers: ", output_layers)

    return output_layers


def draw_prediction(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    # print("Drawing prediction called")

    label = str(classes[class_id])

    color = COLORS[class_id]

    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)

    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    
# image = cv2.imread(args.image)
# image = cv2.read(0)
while True:
    hasFrame,image=video.read()

    # print("Image readed")

    Width = image.shape[1]
    Height = image.shape[0]
    scale = 0.00392

    classes = None

    with open(classes_path, 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

    net = cv2.dnn.readNet(weights_path, config_path)

    blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

    net.setInput(blob)

    outs = net.forward(get_output_layers(net))

    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4

    # print("Processing output layers called")

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

    # print("Processing output layers ended")

    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    for i in indices:
        # i = i[0]
        i = i
        box = boxes[i]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]
        draw_prediction(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))
        objectname = str(classes[class_ids[i]])
        print("Class ID : ", objectname , "Confidence : ", confidences[i])
        if objectname in dangerous_objects and confidences[i] > 0.9:
            
            msg = "Alert, Dangerous object detected " + objectname
            print(msg)

            engine = pyttsx3.init()
            engine.say(msg)
            engine.runAndWait()

            # server = "http://localhost:8000/speak/?message=" + msg
            # try:
            #     res = requests.get(server)
            #     if res:
            #         print("Speech output sent")
            #     else:
            #         print("Speech output not sent, ensure server is running")
            # except Exception as e:
            #     print(e)
            #     print("Error while sending request, Ensure server is running")
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # cv2.imshow("object detection", image)
    # cv2.waitKey()
        
    # cv2.imwrite("object-detection.jpg", image)
    # cv2.destroyAllWindows()
