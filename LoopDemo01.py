#Loops are structures used to repeat sections of code
#They are useful if you have to do the same thing more than once
#or you can establish a pattern

#Example 1:
print("0")
print("1")
print("2")
print("3")
print("4")
print("***********")
	
#This is counted loop. I want you to think about
#count, check, change
# i = 0, 0 < 5

for i in range(4,12,2):
	print(i*2)

print("***********BACKWARDS***********")

for i in range(10,-1,-1):
	print(i)

	print("***********Printing String Characters*****")
	str = "Monkey!!!!!!!"

for i in range(0, len(str), 1):
	print(str[i])



print("MOVING ON")

print("***********PRINT STRING IN REVERSE***********")
for i in range(len(str) - 1, - 1, -1):
	print(str[i])


print("***********PRINT EVERY SECOND LETTER IN STR START AT INDEX 0*****")

