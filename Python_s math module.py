#  python's Math Module

'''
#  Round is a built in Python function 
    #  it is used to round off any number to the neares integer.
'''
# for example

a = round(1.7)
print(a)

# Using Math Module Now!!!

import math

#  while using the round function is the number above the range of .5 give the next integer.          

# For Example 

num1 = round(1.5)
print(num1)
# gives the value 2  

#  while using the floor function of math module in python gives the minimum value of round off 

#  for example 

num2 = math.floor(1.7) 
print(num2)
# It gives the value 1

# and and and !!!! if we use the cei function of math module in the pytghon language it gives the round off the bigger number 

# for example 

num3 = math.ceil(1.7)
print(num3)
#  this gives the round off output 2

'''
___________________

'''

#  to print the value of pi we can use the pi function of math module.        

# for example

num4 = math.pi
print(num4)

# to print the value of e i.e. exponential we can use e function of math module.

# for example 

print(math.e)
# gives the value of exponential

'''
__________________

'''

#  python math modules also has the functons like sin, cos and tan as well as inverse trignometry function
#  they does not take the number in greece whereas they take number in radiants

# they are used in the following way:-

math.sin(math.pi/2)
math.asin(0)
math.cos(0)
math.acos(0)
math.tan(1)
math.atan(1)


#  to find square roots we use hypot function.        

# for example

print(math.hypot(3,4))
# square of 3 is 9 
# square of 4 is 16
# both's addition is 25 
# and square root of 25 is 5
# So here the output is 5.0

# to find cube or squares pow function is used
# but we can also use ** operator without math module to get exponents.      

# for example

print(math.pow(2,5))
# gives output 32.0


math.exp(2)
# gives the 2 multiplied by mapier's constant


# log functions returns the natural logarithm of different numbers
math.log(math.e)

math.log2(8)
