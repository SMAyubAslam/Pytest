#Natural Number > 1
#which has 2 factors 1 and itself

#19 =>  1 and 19 => Prime Number
#28 =>  1,2,,4,7,14,28 => not a prime number

num = int(input('Enter number : '))
count = 0

for i in range(1, num+1):
    if(num%i==0):
        count = count + 1

if count == 2:
    print("Number is prime...")
else:
    print('Number is not prime')