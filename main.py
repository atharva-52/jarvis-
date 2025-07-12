import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio
import pipwin
import musicLibrary
# import openai
# from openai import OpenAI
from newsapi import NewsApiClient
import requests
from gtts import gTTS
import os
import pygame

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak_old(text):

    # engine.setProperty('rate', 125)     # setting up new voice rate
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def  processCommand(command):
    if "google" in command.lower():
        webbrowser.open("https://google.com")

    elif "instagram" in command.lower():
        webbrowser.open("https://instagram.com")

    elif "youtube" in command.lower():
        webbrowser.open("https://youtube.com")

    elif command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in command.lower():

        url = "https://newsapi.org/v2/top-headlines?"
        params = {
            "country": "us",  # Change the country code as needed
            "category": "technology",  # Choose a category (e.g., business, entertainment, etc.)
            "apiKey": api_key
        }

        # Fetch the news
        r = requests.get(url, params)

        # r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                print(article['title'])
                speak(article['title'])



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=1, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
            
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=2, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    processCommand(command)
                    
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout period.")





