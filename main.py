#  Loops In Python

# While Loops
'''
What is while loop?

The  while loop keeps running the same piece of code until the given condition is True , but if the condition is false it won't run.

For example :- 

while True:
    print("Hello")

# Gives the output printing unlimited "Hello"

We can also combines logic with loops.


List can be also combined with the loop to make user insert data or delete data continuosly.

Loops are mostly used to automate the tasks.
'''
# live example to print the 10 numbers with the while loop

number = 1
while number <= 5:
    print(number)
    number = number + 1


'''
# # For Loops # #

A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). ... With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.



'''
# Live example of For Loop

# For integer
for number in range(1,5):
# range helps us to type the whole set of data quickly istead of writing the whole list
    print(number)

# For strings
for letter in "abcd":
    print(letter)


# combining the logic with for loops to get the numbers of vowels and consonants in any strings:

vowels = 0
consonants = 0

for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == "":
        pass
    else:
        consonants = consonants + 1

print(f"Vowel : {vowels}")
print(f"Consonants : {consonants}")



# Combining the dictonaries and lists with the for loops to print the name with only a letter in  them

students = {
    "male": ["Tom" , "Harry" , "Charlie" , "Frank"] , 
    "female" : ["sarah" , "Huda" , "Samantha" , "emily" , "elizabeth"]
}

for key in students.keys():
# It will access the keys of dictonary students
    for name in students[key]:
    # it access the name (i.e. value of key inside the list)
        if "a" in name :
        # identifies the names with letter "a" in every iteration of loop
            print(name)
            # prints the names with "a" in them after identification of names on every iteration of loop



# Note :- For Loops Are very important learn it and give it the higher importance...




'''
list comprehensions:


A list comprehension is a syntactic construct available in Python for creating a list based on existing lists. It follows the form of mathematical set builder notation as distinct from the use of map and filter functions



It is used to create the list based on existing data using for loops, while loops and logic statements combined
'''

# For example

even_number = [x for x in range(1,101) if x % 2 == 0]
print(even_number)


# odd numbers
odd_number = [x for x in range(1, 101) if x % 2 != 0]
print(odd_number)


# For getting the upper case, lower case and length of  word in a single list of list

words = ["hello" , "I" , "am" , "Jenish"]

answer = [[w.upper(), w.lower() , len(w)] for w in words]
print(answer)