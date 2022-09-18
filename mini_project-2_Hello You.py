'''
In this project I have used to input() function of python!!!
'''




# ask for username
username = input("Please enter your username ==> ")


# ask for user age
age = input("please input your age ==> ")


# Ask for user city
city = str(input("Please Input Your city's Name ==> "))


#  ask user what they enjoy
hobbies = input("Please input Your Hobbies here ==> ")



# Create Output Text
string = "Your name is {} and you are {} years old.You live in {} and you enjoy {}"
output = string.format(username,age,city,hobbies)

#  print Output text
print(output)


