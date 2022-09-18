# Password Generator
import random

num_list = "1234567890"
alpha_list = "abcdefghijklmnopqrstuvwxyz"

i = 0

while i<10:

    i = i +1
    letter1 = random.choice(alpha_list)
    letter2 = random.choice(num_list)
    letter3 = random.choice(alpha_list)
    letter4 = random.choice(alpha_list)
    letter5 = random.choice(num_list)
    letter6 = random.choice(alpha_list)
    letter7 = random.choice(num_list)
    letter8 = random.choice(alpha_list)

    password = letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7 + letter8

    print("Password : " + str(password))

