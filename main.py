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
 
#WAP in which escape sequences are being used.

a = "Dear Ishan, You're not Noice! Thanks"
print(a)

formattedLetter = "Dear Ishan,\n\t You're not Noice!\n Thanks"
print(formattedLetter)