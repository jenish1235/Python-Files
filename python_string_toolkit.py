# Some Special String Methods

# String methods are written as           

# string.method()

# # For Example :-

"hello".count('e')
# gives output 1 because e happened once in the hello word.



'''To create the uppercase string and lower case string'''

# string.upper()  --> is used to create the upper case string.

# For Example:-
x = "man"
print(x.upper())
#  gives output MAN.



# string.lower() --> is used to create the lower case string

# for example:-

y = "MAN"
print(y.lower())
# gives output man


# string.capitalize() --> is used to make the first letter of first word of string capital.

# for example:-

z = "happy birthday"
print(z.capitalize())



# string.title() --> is used to make all the first letters of all the words capital in a string.

# for example:-

a = "happy birthday"
print(a.title())


# to check various conditions in string like:-
# text is title --> string.istitle()
#  text is all alphabet --> string.isalpha()
# text is digit --> string.isdigit()
# text is uppercase --> string.isupper()
# text is lowercase --> string.islower()
# text is alpha numeric --> string.isalnum()



# # Note :- Space character doesn't means it is alphabet or number. # #

'''
_________________________

'''

#  to search the piece of string
# is known as string index also ...      
# string.index("part of string to be searched for !!!")

# Note:- String indexing starts with 0.   

# for example:-

x = "happy birthday"
print(x.index("birthday"))

# string.find() is also used to be on the safer side and dont make the program crash due to indexing error

# string.strip() funtion is used to delete the parts strings temporarily...  

# len() is used to find out the length of string

# strip method can be used at the end on input method too strip of the extra spaces given by the user to prevent program from further spaces.





'''
_________________________

# SLICES
'''

# what are slices ?
# split idex is used to split off the one character from string whereas the slicer is used to slice of the part of strings

# for example
word = "jenish"
word2 = word[0:3:1]
print(word2)

word[::-1]
# used to reverse off the whole string.

#  we can use index function to count the index of slice part
