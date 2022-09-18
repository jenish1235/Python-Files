import pyttsx3 
import speech_recognition as sr #pip install speechRecognition


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

print("Please Input Your Name")
speak("please Input your name")
name = input()
print("Please Input Your Gf's Name")
speak("Please input your girlfriend's Name Here")
gf = input()

if __name__ == "__main__":
    
    while True:
    # if 1:
        query = takeCommand().lower()
            
        # Logic for executing tasks based on query
        if 'hello' in query:
            speak("Hello " + name)

        elif 'who are you' in query:
            speak(f"I am {gf}, {name}'s Virtual Girlfriend Made by Jenish")
            print(f"I am {gf}, {name}'s Virtual Girlfriend Made by Jenish")

        elif 'whom do you love' in query:
            speak(f"I love {name}, he is the best boyfriend in the world")

        elif 'what can you do' in query:
            speak(f"I can cook food for {name}")  


        elif 'what are you doing' in query:
            speak("I am Talking to you")

        elif f'who is {name}' in query:
            speak("He is my boyfriend")

        elif 'what is your relationship' in query:
           speak(f"I am {name}'s girlfriend and he is my boyfriend , We are going to marry soon")

        elif 'i love you' in query:
            speak(f"Ohh! I am happy to here that you love me I love you too {name}")    
