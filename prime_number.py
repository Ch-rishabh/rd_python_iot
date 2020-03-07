#prime number

num = int(input("Enter a number : "))

'''isPrime = True

for i in range(2, (num // 2) + 1):
    if num % i == 0:
        isPrime = False
        print("Number is not prime")
        break
if isPrime:
    print("Number is prime")'''

for i in range(2, (num // 2) + 1):
    if num % i == 0:
        isPrime = False
        print("Number is not prime")
        break
else:
    print("Number is prime")
