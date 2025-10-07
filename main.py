import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

# pip install pocketsphinx

recognizer=sr.Recognizer()
engine = pyttsx3.init()
newsapi = "5b3bddb35eb94a2798c19efc6edd6e00"

def speak_old(text): #function to speak the text passed to it
    engine.say(text)
    engine.runAndWait()   

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')


    # Initialize the mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

    # Play the music
    pygame.mixer.music.play()

    # Keep the program running so the music can play
    while pygame.mixer.music.get_busy():  # Check if music is still playing
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")  # Clean up the temporary file


def aiProcess(command): #function to process the command using OpenAI
    client = OpenAI (api_key="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",
    ) #billed api key is needed for gpt-4 (free trial keys will not work) 


    completion = client.chat.completions.create(    
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": "You are virtual assistant named Nova skilled in explaining general tasks like Alexa and Gemini  in simple terms with creative fair.Give short and concise responses please."},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

def processCommand(c): #function to process the command
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "open youtube" in c.lower():
        speak("Opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open linkedin" in c.lower():
        speak("Opening linkedin")
        webbrowser.open("https://www.linkedin.com")
    elif  c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}") #uses the newsapi to get the top headlines in india
        if r.status_code == 200:
            # parse the json response
            data = r.json()

            #extract the articles
            articles = data.get('articles', [])

            # print the headlines
            for article in articles:
                speak(article['title'])
    
    else:
        output = aiProcess(c)
        speak(output)


if __name__=="__main__":
    speak("Initializing Nova") 
    while True:
        #Listen for wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=1, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower()=="nova"):
                speak("Yeah! How can I help you?")
                # time.sleep(1)
                #listen for command
                with sr.Microphone() as source:
                    print("Nova is Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))