import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Mam !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Mam !")

	else:
		speak("Good Evening Mam !")

	assname =("Keran 1 point o")
	speak("I am your Assistant")
	speak(assname)
def username():

	speak("What should i call you Mam")
	uname = takeCommand()
	speak("Welcome Mam")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mrs.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Mam")

def take_command():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"

    return query

if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
	# command before execution of this python file

    clear()
    wishMe()
    # username()
	   
    while True:

        query = take_command().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'who are you' in query:
            speak("I am Keran developed by Aakansha Kansal")
        elif 'who developed you' in query:
            speak("I am Keran developed by Aakansha Kansal")
        elif 'who created you' in query:
            speak("I am Keran developed by Aakansha Kansal")
        elif 'how are you' in query:
            speak("I am great how are you")
        elif 'i love you' in query:
            speak("I love you too")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://www.google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("https://www.github.com")
        elif 'open geeks' in query:
            speak("opening geeks")
            webbrowser.open("https://www.github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("https://www.stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("https://www.spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/.com")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("https://gaana.com/")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'sleep' in query:
            exit(0)