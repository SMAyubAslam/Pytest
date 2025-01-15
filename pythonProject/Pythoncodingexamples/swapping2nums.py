# How To Swap 2 Numbers

num1 = int(input('Enter num1 value : '))
num2 = int(input('Enter num2 value : '))

print("Value of num1 before swapping ", num1)
print("Value of num2 before swapping ", num2)

#Approach 1
# temp = num1
# num1 = num2
# num2 = temp

#Approach 2
num1,num2 = num2,num1

print("Value of num1 after swapping ", num1)
print("Value of num2 after swapping ", num2)
