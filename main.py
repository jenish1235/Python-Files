# Python Data structures make it possible to store large amount of data in a single variable and hel to access it within one line of code.


# # Lists # #

'''
#  How to create a list ?

==> The list can be created using the square brackets.
For example:-
our_list = [13,15,17]


# Note :- Python Lists unlike the list in other languages can have the multiple datatypes inside it . i.e. :-

our_list2 = ["a",12,"b","cd"] 
# This list is also valid


#  The lists are iteral data types just like string are.

# So, the list also have there own indexing system which starts from 0, and can be broken into the elements

For example

our_list3 = ["a",12,"b"]
our_list3[1]
# will give the output 12 because of indexing position 1


# If we want to take out multiple elements from the list we can use the slices function as same as strings .

# Note:- List can also have other list inside themselves too.  

For example:-

multiple_list = [0,10,["a","b","c"], 90 ,12]

for indexing of another list in the one list :-

as in the above example the indexing of the above list is 2 . So, 

multiple_list[2]
# gives the output ["a","b","c"]

to access the data inside the list of 1 list can be done like this:

multiple_list[2][2]
# Gives the output  "c" as the indexing of c inside the second list is 2....


# # list can be used to create the tables in the python as the two cordinates for slices out the data from the list acts as the row and columns.

### List can be sliced in the multiple types as same as strings So do try by yourself making multiple combinations ###

del keyword can be used to delete the slice of data from list(but need the indexing values )
&&
remove keyword is used to remove the specific data only

There are more ways to add data to the list too.

1) it can be done using the addition operator .(but in this mthod only lists can be added to the lists and not the strings or inntegers.)

For example:- 

a = [5,6,7,8]

a = a + 9         
# is not valid while

a = a + [9]
# is valid

2) list method can be used to enter the strings as characterwise eleents to the list .   

For example:- 

a = [5,6,7,8]
a = a + ["BCD"]
# will give output
[5,6,7,8,"BCD"]

# while 

a = a + list("BCD")
# will give output
[5,6,7,8,"B","C","D"]

(We cant use the list function for the integers as they are not iterable datatype. But if we first convert the integer to the string then we can use the list functionality to add the number to the list as they become the strings )


3) To add a list as the element of the list

a = [5,6,7,8]
a = a + [[1,2,3,4]]
# will add the [1,2,3,4] as a single element to the list


4) to insert the data at the particular indexing space in the list 

insert functionality can be used

for example :- 

a = [4,6,7,8]
to enter 5 between the 4 and 6 in the list a :-

a.insert(1, 5)
insert functionality takes the 2 or more than 2 arguments to deal with

the first argument is always the indexing position of data to be entered
and then after all the arguments are the data to be inserted into the list.

note:- insert function does not need the syntax of a = a.insert(). 

'''


'''
_______________________________

'''




# # Tuples # # 
'''
# What is the tuple ?
tuple is mostly like the list the  main difference is they cannot be changed after they are made.    

#  tuple does not support item assignment as ssame as strings

# tuple are called the imutable datatype

for example:-

our_tuple = 1,2,3,4,"a","A"
our_tuple = (1,2,3,4,"a","A")

# both are valid

# they can be also sliced as same as strings and the list

# tuples can also store all types of datatypes

They are mostly used for storing the data which never needs to be changed to prevent the accidental change of data

''' 


# # Dictonaries # #

'''
Dictonaries are the complete game changer python datatype...

Making a dictonary:

a = {}
a = {"Jenish":15, "Jaisiddh" : 16 , "Abhishek": 17}
# We have to give the keys and then append the values to the keys
# in the above example "Jenish" is the key and the 15 is value of key

To get return the value of any key from the dictonary :

a["Jenish"] will give the value of "Jenish" key in the dictonary a

i.e = 15

To Assign some new key and value to the dictonary:

a["dhruv"] = 20
# The "dhruv" key is added with the value of 20 in the dictonary a .

to check :
#  we can try printng the dhruv key from dictonary a:

a["dhruv"] 

# will return the output 20

------------------------------------

We can also update the value the same way we add the key and value




by putting del keyword in the starting of the adding function we can del any key from the dictonary

# # Dictonaries does not support indexing.



For indexing we can convert the dictonary to the list :

a = list(a.keys())
# gives the acess to the keys in the list form


.items() function is used to pull out all the tems from the dictonary and show it as a output

# # Giving Multiple values To the single keys


'''
# Dictonaries Assigning Multiple Values to The Single Keys

'''
Instead of assigning a single value or you can say single integer we can assign a complete list to the key of dictonary :

dict_items = {}
dict_items = {a: (1,2,3), b: (4,5,6),  } 
we can use indexing for printing the single list items

Instead of having list as a value of a key we can also give another dictonary to the key of first dictonary .

syntax:

a = {}
a = { "a" : {age: 1, id: 2,}}

print(a["a"]["age"])
give output 1
'''


# Multiple Variables With a Single go:-

a,b,c = (1,2,3)
# is valid
a = 1
b = 2
c = 3







