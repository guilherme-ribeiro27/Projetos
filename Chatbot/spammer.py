import pyautogui as py
import time
import csv

#script = open(r"C:\Users\Guilherme\Desktop\Jogo em Python\Chatbot\beemoviescript")
script = open(r"C:\Users\Guilherme\Desktop\Jogo em Python\Chatbot\herecomesthesun")
time.sleep(5)

for word in script:
    py.typewrite(word)
    time.sleep(0.5)
    py.press('Enter')