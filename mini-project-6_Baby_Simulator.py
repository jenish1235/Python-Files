# Funny Baby Conversation Simulator 
from random import choice
import pyttsx3
questions = ["Why should i sleep: ", "why is sky blue in color: " , "why are you happy: " , "why should I study: "]
question = choice(questions)
answer = input(question).lower().strip()

while True:
    if answer != "just because":
       why = input("Why?: ").lower().strip()
       if why == "just because":
           print("Thank You so much ! Now I have understood")
           pyttsx3.speak("Thank You so much ! Now I have understood")
           break

    elif answer == "just because":
        print("Thank You so much ! Now I have understood")
        pyttsx3.speak("Thank You so much ! Now I have understood")
        break
