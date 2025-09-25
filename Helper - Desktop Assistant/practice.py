import speech_recognition as sr
import pyttsx3
import musiclibrary
import webbrowser
import requests
from openai import OpenAI



recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "49a7a1799a044765ac8f903f47d46132"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(text):
    client = OpenAI(
    api_key = "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")
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[
        {"role": "system", "content": "You are a helpful assistant skilled in general tasks like alexa and google cloud."},
        {"role": "user", "content": "What is coding?"}])

# ✅ Print the AI's reply
    return completion.choices[0].message.content

def processText(t):
    if "open youtube" in t.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in t.lower():
        webbrowser.open("https://instagram.com")
    elif "open facebook" in t.lower():
        webbrowser.open("https://facebook.com")
    elif  t.lower().startswith("play"):
        song = t.lower().split(" ") [1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in t.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            print(data)
            articles = data.get("articles", [])
            print(f"Total articles fetched: {len(articles)}")

            for article in articles:
                print("Speaking:", article["title"])
                speak(article["title"])

    else:
        output = aiprocess(t)
        speak(output)

                


if __name__ == "__main__":
    speak("Initialising Helper...")

    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        # Use the microphone as source

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=5,phrase_time_limit=5)
                word = r.recognize_google(audio)
                if word.lower() == "helper":
                    speak("Yes,How may i help you")
                    with sr.Microphone() as source:
                        print("Helper Active...")
                        audio = r.listen(source)
                        text = r.recognize_google(audio)
                        processText(text)
        except Exception as e:
            print("Error: {0}".format(e))
