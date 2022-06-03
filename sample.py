import pyttsx3
from os import system

while 1:
    system('say Hello world!')

    engine = pyttsx3.init()
    engine.say('Sally sells seashells by the seashore.')
    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()