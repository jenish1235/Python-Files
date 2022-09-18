# exercise 1

## Create a variable called a and set it equal to 20851 plus 92421 ##

a = 20851 + 92421

## Create a variable called b and set it equal to 90234 minus 4314.5 ##

b = 90234 - 4314.5

# Create a variable called c and set it equal to 5678 multiplied by 2341

c = 5678 * 2341

# Create a variable called d and set it equal to 993 divided by 456

d = 993 / 456


# Create a variable called e and set it equal to the remainder from dividing 500 by 3 

e = 500 % 3


'''
________________
exercise 2

'''


# First create a variable called x and set it equal to any number
x = 5
# Next create a variable called y and set it equal to any number

y = 10
# Now, create a variable called z and set it equal to x + y

z = x + y
# Now overwrite the value of x with the value of z

x = z
# Finally, print x to the screen using python's print function
print(x)





'''
________________
exercise 3

'''

# First, create a variable called start, and set it equal to "I am ".
# Remember the space after the word "am" !

start = "I am "

# Next, create a variable called age and set it equal to your age in years.
# This must be a number

age = "15"

# Next, create a variable called end, and set it equal to " years old".
# Remember the space before the word "years"

end = " years old"

# Next, create a variable called output and use {} symbols and the format() function to stick the start, age and end variables
# together to make a string.

output = "{}{}{}".format(start,age,end)

# An example output string would be "I am 15 years old"


# Finally, print the output to the screen using the print() function.

print(output)




'''
_________________
exercise 4

'''

# Create a variable called name and set it equal to your name

name = "jenish"

# Create a variable called age and set it equal to your age

age = 15

# Create a variable called output, and use {} symbols and the format() function to 
# make it contain a string like the example text in the description

output = "My name is {} and I am {} years old.".format(name,age)


# Finally, use the print() function to print the output.

print(output)



'''
_________________
exercise 5

'''


# here is a very long word

word = "antidisestablishmentarianism"

# use a slice to take out the word "establishment"
answer = word[word.index("est"):word.index("ment") + 4 :1]
print(answer)
# and store it in the answer variable....
