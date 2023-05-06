import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)

def speak(audio):
    engine.setProperty('rate', 180)
    engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour= int(datetime.datetime.now().hour)
    if(hour>=12 and hour<24):
        speak("Good Evening")
    else:
        speak("Good Morning")
    speak("I am Tokyo Sir")
    speak("Please Tell me How may I help You")
def takeCommand():
    '''
    '''
    r= sr.Recognizer()
    with sr.Microphone() as source:
        speak("I am Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        speak("Recognizing")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e :
        print(e)
        speak('Say that again please....')
        return "None"
    return query
if __name__=="__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'stop' in query:
            break
        elif 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe"
            wb.get(chrome_path)
            wb.open("youtube.com")
        elif 'play music' in query:
            music_dir=



    


