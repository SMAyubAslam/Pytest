#5! = 1 * 2  * 3 * 4 * 5
#Recursive approach

def factorial(n):
    # if n == 1 or n == 0:
    #     return 1
    # else:
    #     return n * factorial(n-1)
    #Ternary Operator
    return 1 if(n==1 or n==0) else n * factorial(n-1)

num = int(input("Enter a num : "))
print("Factorial of", num, "is", factorial(num))