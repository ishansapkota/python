#  WAP to display the poem "Twinkle twinkle little star"
# print('''Twinkle twinkle little star 
# How I wonder what you are
# Up above the world so high
# Like a diamond in the sky''')

#WAP to print the contents of directory using OS module.

import os

# print(os.listdir())
# # print(os.getcwd())
# os.chdir('C:\\Users')
# print(os.getcwd()

import os
from pyclbr import Function

# a = input("Enter the number: ") this is how you take inputs in python

# s = int(a)
# print("The sum of a and a is: ", s+s)

# print(type(s))
# print(type(a))

a = "ISHAN"

# print(a[2:3]) 
'''this ':' sign helps in slicing the string where the previous index is included in the output
but the end index is not included in the output'''  

# print(a[:5]) #this is equivalent to a[0:5]
# print(a[0:]) #this equivalent to a[0:last index] and this gives the whole string as the final output

'''in array a = "ISHAN"
    I = [0]
    S = [1]
    H = [2]
    A = [3]
    N = [4]

    But as we know the index of last term is -1 so, we can also write
    I = [-5]
    S = [-4]
    H = [-3]
    A = [-2]
    N = [-1] 

    so,
'''

# print(a[0:4])
# print(a[-5:-1])
# # these two are the same

#string function

# a = '''my name is Ishan Raj Sapkota. I am currently studying Computer Engineering in 
# Nepal College of Information and Technology.'''

# print(len(a))
# print(a.endswith("."))
# print(a.count("I"))
# print(a.capitalize())
# print(a.find("Ishan")) #if the words are repeated then it only gives the index of the first occurance notall
# print(a.replace("Nepal College of Information and Technology", "Harvard"))


#ESCAPE SEQUENCES
#the escape sequences are: \n \t \\ \' etc
# a = "My name is Ishan Raj.\n  \tI am a \'twat\'\\\'cunt\'."
# print(a)

#WAP to display a user defined name followed by Good Afternoon.

# a = input("Enter a name: ")

# print(a + ", Good Afternoon")

#WAP to display the letter template given:
# letter = ('''Dear |<NAME>|
#         , you are selected! |<DATE>|''')

# name = input()
# date = input()
# letter = letter.replace("|<NAME>|", name)
# letter= letter.replace("|<DATE>|", date)
# print(letter)

#WAP to find double spaces in the string 

# a = "My  name is Ishan."

# # doubleSpaces = a.find("  ")
# # print(doubleSpaces) #this helps to find the index of the character we're searching for

# #WAP to replace the double space with single space

# doubleSpace = a.replace("  "," ")
# print(doubleSpace)
 
# #WAP in which escape sequences are being used.

# a = "Dear Ishan, You're not Noice! Thanks"
# print(a)

# formattedLetter = "Dear Ishan,\n\t You're not Noice!\n Thanks"
# print(formattedLetter)


#LISTS AND TUPLES

'''Lists are the collection of data and it is initialized by the square bracket [], lists are in ordered form.
The data inside the lists can be of any datatype for eg:'''
# list1 = [25,"Ishan Raj",False]

# print(list1[0])

# #IN lists we can update the values in list
# list1[0] = 191325
# print(list1)

# #LIST SLICING 
# #list slicing is the same as the string slicing
# friends = ["Ishan","Sudip","Unique",45,5,56]
# print(friends[-4:-1])

#LIST METHODS
# the list methods changes the root value unlike the string functions
# list1 = [1,4,5,2,7]
# list1.sort() #--> this sorts the list in ascending order
# list1.reverse() #--> this reverses the order of the list
# list1.append(8) #this inserts the given value i.e 8 at the end of the list
# list1.insert(2,30) #in this, the first value i.e 2 is the index of the list and second value i.e 30 is the value to be inserted
# list1.pop(2) #this method pops the value at the index 2, this works with the index
# list1.remove(7)  #this removes the value 7 from the list 
# print(list1)


#TUPLES

# A tuple is the collection of data like lists but it is initialized with small bracket () and unlike lists it cannot update or override the given value but like lists it can store any type of datatype inside of it.
#tuple is given below:

t1 = (1,2,3,10,3)
print(t1)

#in the case of tuple we cannnot provide only one element like the example given below:
t1 = (1) #it reads the given expression as the value of a variable but not a tuple so when we'll have to give the single element tuple we would have to do the following.

t1 = (1,)

#TUPLE METHODS

t=(1,2,3,1,2,6,4,3)

print(t.count(1))   #gives the count of the given value i.e 1 in the tuple
print(t.index(3))   #gives the index of the value given i.e 3 in the tuple

# Function

def Hello(): #function is defined in this way 
    print("Hello")