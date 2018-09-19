import os

#we use the input function to take an input
#we have to have an assignment statement to store an input

#input is a function. It runs a small program that
#causes the computer to stop and wait for input
fName = input ("what is your name: ")
lName = input ("what is your last name: ")

print("Hi, "+fName+" "+lName)
print("Hi "+fName)
initialName = fName[0] + "." + lName #adding strings is concatination
print("Hi, "+initialName)

os.system("say "+fName+" "+lName)