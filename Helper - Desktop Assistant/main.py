import speech_recognition as sr
import musiclibrary
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def Process_Command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)


    


if __name__ == "__main__":
    speak("initialising Helper....")
    while True:
        r = sr.Recognizer()

        # Use the microphone as source
    
        print("🧠 Recognizing...")
        try:
            with sr.Microphone() as source:
                print("🎙️ listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "helper":
                speak("Yes,how may i help you")
                #listen for command
                with sr.Microphone() as source:
                    print("Helper Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    Process_Command(command)
        except Exception as e:
            print("Error; {0}".format(e))
