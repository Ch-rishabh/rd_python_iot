a = 10
b = 20
c = a + b
'''print("A is" + str(a) + "b is" + str(b))
print("A is",a,"b is",b)
print("A is %d"%a)
print("Sum of %d and %d is %d"%(a,b,c))'''
print("Sum of %d and %d is %s"%(a,b,"10"))

num = 0
print("Sum of {} and {} is {}. Total result is {}".format(a,b,c,c))
print("Sum of {0} and {1} is {2}. Total result is {2}".format(a,b,c))
#print("Sum of {2} and {1} is {0}".format(c,b,a))

name = input("Enter your name : ")
print("Name is", name)
print(f"Name is {name}")
print(f"{name}")

index = 0
arr = [1,2,3,4,5]
print(f"First element is {arr[index]}")
