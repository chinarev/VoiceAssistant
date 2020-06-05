import speech_recognition as sr
import os
import sys
import webbrowser
import win32com.client as wincl
import pyaudio

speak = wincl.Dispatch("SAPI.SpVoice")


def talk(words):
    print(words)
    speak.Speak(words)

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1 #Слушаем 1 секунду
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + task)
    except sr.UnknownValueError:
        talk("Не понимаю")
        task = command()
    return task

def makeSomething(task):
    if 'открыть гугл' in task:
        talk("Ок, отрываю")
        url = 'https://google.com'
        webbrowser.open(url)
    elif 'открыть яндекс' in task:
        talk("Ок, отрываю")
        url = 'https://yandex.ru'
        webbrowser.open(url)
    elif 'стоп' in task:
        talk("Окей, закрываюсь")
        sys.exit()

while True:
    makeSomething(command())



