# Functions in Python

'''
What is the functions?

--> A function is the block of organised and the reusable code

We use the "def" keyeord to create the function and "return" keyword is used to get the output of what the function did...

For example:-

1) Creating a simple function to add two numbers
'''
def add(x, y):
   return x+y

'''
To run the function we have to call the function

for example:- 
2) Calling the add function we have created earlier
'''
add(5,10)


'''
A single function can be used multiple times in the code


Note :- Returning the value and printing the value is different .

print statement just shows the output on theconsole screen and it doesn't stores the ddata inside the computer's memory to be used later whie the return statements are used to store the data obtained by the process of the function called and can be used by computer in the later processing.

'''

# defining the function which returns the reversed text 

def rev(text):
    return text[::-1]


'''
# Variable Scope

There are mainly 2 types of variable scopes:
1. Global Scope:It can be seen globally throughout your code. Variable is called Global Variable

2. Local Scope:

'''
# For example:

# learning the variable scopes

a = 100

def f1():
    print(a)

def f2():
    print(a)
# Here in the above example the a is the global variable and therefore the output is the 100 printed on the console 2 times. This is the global Scope. Let's Re-create the functions using local scope.

def f1():
    a = 100
    print(a)

def f2():
    a = 50
    print(a)

# In the above example the a is local variable using the local scope and the output is 100,50 as expected on the console.


'''
Note :- local variables cannot be changed the from the outside of the function and they are destriyed in the end of particular variable.They are cannot be used from the outside of function.

The global scopes can't be edited by the insid eof the functions while they can be accessed from the any part of code whether it is function or a loop or a logic system.

But the global method is used to edit the global variable from inside the function:

a = 100
def f1():
    global a 
    a = 200
    print(a)

this program will give the output 200 on editting the global variabble from inside of the function.

Note: Functions only creates the local variables using the local scope but the loops and logic statements doesn't.
'''

# # Keyword Arguments And Default Parameter

'''
Lets create a funtion to understand the keywords and the arguments!!!!
'''
def about(name, age, likes):
    sentence = "meet {}! They are {} years old and they like {}".format(name,age,likes)
    return sentence

# here in the above example name age and likes are keyword and while we call the funtion in our program we will have to provide the certain data as per asked by keywords of the function and that data will be know as arguments 
# for example:

about("jack",20,"python")

# here the "jack" , 20 and "python" are the argument which needs to be provided by the user


'''

# How can we make the function without giving the argument ?
# 
# We can put the default value which will be always used if the user doesn't passes the argument
# 
# But it is to remembered that all the default parameters have to given in the last while asigning the keywords
# 
# 
# For Example:- 
# 
'''
def about(name,age,likes="python"):
    print(name,age,likes)

# Here in the example likes  = "python" is a default parameter an it needs to be given at last while defining the function.



'''
# Packing and Unpacking Variables

# Unpacking Arguments

'''

print(1,2,3,4,5)
# It will print : 1 2 3 4 5

# but if we have a list :
number = [1,2,3,4,5]
print(number)
# it will print : [1,2,3,4,5]

# but if we want the number list unpacked and get each argument personally
print(*number)
# it will unpack the arguments in the variable numbers and will print: 1 2 3 4 5

# Unpacking can be used with the string too.




'''
# Packing the arguments

'''

# it can be used to pack the aguments when you dont know how many arguments will be provided by the user

'''
Unpacking Keyword Argument

# It basicall works on the dictonaries
'''
# for example:
# 
def about(name,age,likes):
    print(name,age,likes)


# now if we have dictonary and if we want to unpack the data of the dictonary into the keyword arguments:

dict_a = {"name": "jack", "age": 20 , "likes":"python"}

# We will have to use *^2 for unpacking the dictonary in the keyword arguments:

about(**dict_a)

'''
Packing the keyword arguments
'''
def fun(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key,value))

fun(a= "a" , b = "b")




