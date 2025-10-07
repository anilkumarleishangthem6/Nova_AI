import speech_recognition as sr
import pyttsx3
import time

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    recognizer = sr.Recognizer()
    while True:
        print("Listening for wake word...")
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
            word = recognizer.recognize_google(audio)
            print(f"Recognized: {word}")
            if word.lower() == "jarvis":
                speak("Yahh...how can I help you?")
                time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")