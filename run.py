#!/usr/bin/env python3

import time
import speech_recognition as sr
import pyttsx3

class Ser:

    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        self.engine = pyttsx3.init()
        self.engine.connect('started-utterance', lambda name: self.stop())
        self.engine.connect('finished-utterance', lambda name, completed: self.listen())

    def _callback(self, recognizer, audio):
        print("Heard something...")
        try:
            words = recognizer.recognize_google(audio, language="fi-FI").lower()
            print(words)
            if "tietokone" in words:
                if "hei" in words:
                    self.say("Well, hello there!")
                elif "lopeta" in words:
                    print("Moro...")
                elif "aika" in words or "kello" in words:
                    timeis = "Kello on " + time.ctime()
                    print(timeis)
                    self.say(timeis)
                else:
                    self.say("En ymmärrä: " + words)
        except sr.UnknownValueError:
            print("What?")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def listen(self):
        print("Starting to listen...")
        self.m = sr.Microphone()
        print("Adjusting...")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
        self.stop_listening = self.r.listen_in_background(self.m, lambda recognizer, audio: self._callback(recognizer, audio))
        print("GO!")

    def start(self):
        self.listen();
        self.engine.startLoop()
        self.listening = True
        while self.listening:
            self.engine.iterate()
        self.endLoop()
        self.stop()

    def stop(self):
        print("Stopped listening...")
        self.stop_listening()

    def say(self, msg):
        print("Speaking: " + msg)
        self.engine.say(msg)

pop = Ser()

pop.start();
