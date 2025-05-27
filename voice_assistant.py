from http import server

from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import requests


# from jarvis_ai import sendEmail

newsApi = "a23fae92555e4cd894cf3ca2f8b580bd"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")

    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hello sir i am alexa how may i help you")


def takeCommand():
    # it take microphone input from the user and return string command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print (e)
        print("say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    try:

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('pekodora6@gmail.com', 'dehugiagobihqgnd')
        server.sendmail('pekodora6@gmail.com', to, content)
        server.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # speak("This ia a group project by Aditya Sharma , Balkrishna jha and Divyansh Sharma")
    wishMe()
    while True:
        query = takeCommand().lower()  # it will require pyAudio to be installed
        # Logic for executing task based on querry
        if 'wikipedia' in query:

            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to search wikipedia")
            break
        elif 'open youtube' in query:
            webbrowser.open(
                "https://www.youtube.com/results?search_query=salena+jones+gomez+new+song")
            break
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            break
        elif 'play music' in query:
            music_dir = 'C:\\Users\\dell\\Music\\Video Projects'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            break
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = 'C:\\Users\dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
            os.startfile(codePath)
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        elif 'send email' in query:
            try:
                speak("what shout i say?")
                content = takeCommand()
                # content= "Dear Adsdgdsgitya you have been selected for the microsoft placement of 50 lakh ctc"
                to = 'sharmaujjawal546@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                # speak(e)
                speak("sorry aditya sir i am unable to send this email")
            break
        elif 'open news' in query:
            try:
                result = requests.get(
                    f"https://newsapi.org/v2/everything?q=tesla&from=2025-04-16&sortBy=publishedAt&apiKey={newsApi}")
                result = result.json()
                print(len(result['articles']))

                news = result.get('articles', [])[0:5]
                speak("According to news api")
                for i in news:

                    speak(i['title'])

            except Exception as e:
                print(e)
                speak("sorry aditya sir i am unable to search news")
