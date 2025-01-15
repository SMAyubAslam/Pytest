#5! = 1 * 2  * 3 * 4 * 5
#Iterative approach
factorial = 1
num = int(input('Enter a number : '))

if num < 0 :
    print("There is no factorial for negative number")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
    print("Factorial of ",num , "is", factorial)