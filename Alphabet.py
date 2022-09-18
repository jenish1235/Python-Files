import pyttsx3
import speech_recognition as sr
import pyaudio

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice)
engine.setProperty('voices',voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def About():
    myself = "Hello I am a Alphabet Teacher. You can input any alphabet and I can tell You The name of thing related to that alphabet"
    print(myself)
    speak(myself)


About()
while True:
    alphabet = input()
    if(alphabet=="a"):
        apple = "apple"
        print(apple)
        speak(apple)
    elif(alphabet=="b"):
        apple = "banana"
        print(apple)
        speak(apple)
    elif(alphabet=="c"):
        apple = "Cat"
        print(apple)
        speak(apple)
    elif(alphabet=="d"):
        apple = "dog"
        print(apple)
        speak(apple)
    elif(alphabet=="e"):
        apple = "elephant"
        print(apple)
        speak(apple)
    elif(alphabet=="f"):
        apple = "frog"
        print(apple)
        speak(apple)
    elif(alphabet=="g"):
        apple = "Goat"
        print(apple)
        speak(apple)
    elif(alphabet=="h"):
        apple = "Honey"
        print(apple)
        speak(apple)
    elif(alphabet=="i"):
        apple = "ice-cream"
        print(apple)
        speak(apple)
    elif(alphabet=="j"):
        apple = "joker"
        print(apple)
        speak(apple)
    elif(alphabet=="k"):
        apple = "kite"
        print(apple)
        speak(apple)
    elif(alphabet=="l"):
        apple = "lion"
        print(apple)
        speak(apple)
    elif(alphabet=="m"):
        apple = "monkey"
        print(apple)
        speak(apple)
    elif(alphabet=="n"):
        apple = "nose"
        print(apple)
        speak(apple)
    elif(alphabet=="o"):
        apple = "Octopus"
        print(apple)
        speak(apple)
    elif(alphabet=="p"):
        apple = "parrot"
        print(apple)
        speak(apple)
    elif(alphabet=="q"):
        apple = "Queen"
        print(apple)
        speak(apple)
    elif(alphabet=="r"):
        apple = "river"
        print(apple)
        speak(apple)
    elif(alphabet=="s"):
        apple = "sun"
        print(apple)
        speak(apple)
    elif(alphabet=="t"):
        apple = "tortoise"
        print(apple)
        speak(apple)
    elif(alphabet=="u"):
        apple = "umbrella"
        print(apple)
        speak(apple)
    elif(alphabet=="v"):
        apple = "violin"
        print(apple)
        speak(apple)
    elif(alphabet=="w"):
        apple = "watch"
        print(apple)
        speak(apple)
    elif(alphabet=="x"):
        apple = "xylophone"
        print(apple)
        speak(apple)
    elif(alphabet=="y"):
        apple = "yo-yo"
        print(apple)
        speak(apple)
    elif(alphabet=="z"):
        apple = "zebra"
        print(apple)
        speak(apple)
    else:
        print("please reload and enter a valid alphabet")
        speak("please reload and enter a valid alphabet")
        break

speak("A for Apple, B for Ball, C for Cat, D for Dog, E for Elephant, F for Frog, G for Goat, H for Honey, I for Ice-Cream, J for Joker, L for Lion, M for Monkey, N for Nose, O for OctoPus, P for Parrot, Q for Queen , R for River, S for Sun, T for Tortoise, U for Umbrella, V for Violin, W for Watch, X for XyloPhone, Y for Yo-Yo And Z for Zebra")
