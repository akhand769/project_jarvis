import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)

def speak(audio):
    engine.setProperty('rate', 180)
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour= int(datetime.datetime.now().hour)
    if(hour>=12 and hour<24):
        speak("Good Evening")
    else:
        speak("Good Morning")
    speak("I am Max")
    speak("Please Tell me How may I help You Sir")
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.1
        speak("I am listening...")
        audio = r.listen(source)
    try:
        speak("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e :
        print(e)
        speak('Say that again please....')
        return "None"
    return query
def sendEmail(to,body):
    password='sqmdthdagtsiutwx'
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login('akhandchaurasia2002@gmail.com',password)
    server.sendmail('akhandchaurasia2002@gmail.com',to,body)
    server.close()
if __name__=="__main__":
    wishme()
    while True:
        r=sr.Recognizer()
        query2='Hello'
        with sr.Microphone() as source:
            r.pause_threshold = 0.1
            print('listening')
            audio = r.listen(source)
        try:
            query2 = r.recognize_google(audio,language='en-in')
        except Exception as e :
            print(e)
        if query2=='Max':
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
                # chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe"
                # wb.get(chrome_path)
                wb.open("youtube.com")
            elif 'play music' in query:
                music_dir='C:\\Users\\akhan\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
            elif 'current time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(strTime)
            elif 'open vs code' in query:
                codepath="C:\\Users\\akhan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
            elif 'email' in query:
                try:
                    speak("Give me the mail id")
                    mailid = 'akhand769@gmail.com'
                    print(mailid)
                    speak("What is the body")
                    content = takeCommand()
                    print(content)
                    sendEmail(mailid,content)
                    speak("Email sent successfully !!")
                except Exception as e:
                    print(e)
                    speak("Sorry Akhand Email cannot be sent due to some error ")
                    

        



    


