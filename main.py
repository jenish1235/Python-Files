# Object Oriented Programming #

import random
# Classes and Objects



# What Is Object Oriented Programming?
'''
Object Oriented Programming is the method of smart reuse of code unlike functions , but there is difference between OOPs and Function.

'''



# OOPs
'''

# Classes #
--> Classes Are templates of the Objects . They Are A dummy of the objects which can be used regularly for creating the objects...
'''

'''
#Objects
Objects are the instances made using the classes

'''
# Lets Do practical to understand nicely


# Creating The Class 
# class Rupee:
#     value = 1.00 
#     color = "grey"
#     num_edges = 1
#     diameter = 22.5 #mm
#     thickness = 3.15 #mm
#     heads = True

# Objects

# coin1 = Rupee()
# coin2 = Rupee()
# print(coin1.color)
# print(type(coin1))


# To change The Predefined Value For Particular object

# coin1.color = "green"
# coin1.value = 2

# print(coin2.color)
# print(coin1.color)



# Class Methods

'''
---> For Sometime We Have To Give Some Behaviours To Our Objects And This Can Be Done By Giving The Class Methods.


'''

# # Creating the class methods

# class Pound:


#     def __init__(self , rare = False):
        
#         self.rare = rare

#         if self.rare:
#             value = 1
#         else : 
#             value = .5
#         self.value = 1
#         self.color = "Green"
#         self.num_edges = 1
#         self.diameter = 22.5
#         self.thickness = 3.15
#         self.heads = True
    
#     def rust(self):
#         self.color = "Brown"
    
#     def clean(self):
#         self.color = "Green"

#     def flip(self):
#         heads_option = [True, False]

#         choice = random.choice(heads_option)
#         if choice == True:
#             print("heads")
#         else:
#             print("Tails")

# # class Destructor
#     def __del__():
#         print("Coin Spent")

# coin3 = Pound()
# coin3.flip()


'''
def __init__ is a contructor while __del__ is a destructor

'''




# Class Inheritance:

'''
We can Create a general or a genetic class from which every other class can gain thier values.
'''

# For Example:

class Coin:
    def __init__(self , rare = False, clean = True, heads = True, **kwargs):
        
        for key,value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean

        if self.is_rare :
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value


        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color

    
    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print("Coin Spent")

    def flip(self):
        heads_option = [True, False]

        choice = random.choice(heads_option)
        if choice == True:
            print("heads")
        else:
            print("Tails")

# lets give the inheritance to the rupee class in this program

class Rupee(Coin):
    def __init__(self):
        data = {
            "original_value":1.00,
            "clean_color":"Grey",
            "rusty_color": "Brown",
            "num_edges" : 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5,
        }
        super().__init__(**data)