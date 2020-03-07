list1 = [11,22,33,44,55]

'''for i in range(5):
    print("Inside loop")
    print(i)
print("Loop finished")'''

for i in range(len(list1)):
    print(i)
    print(list1[i])

print("***************")

for value in list1:
    print(value+1)
print(list1)

for i in range(len(list1)):
    print(i)
    if i == 2:
        print("Continuing without incrementing")
        continue
    if i == 4:
        print("Going to break the loop")
        break
    print("Going to increment the value")
    list1[i] += 1
print(list1)

a = 10

while a > 0:
    print(a)
    a -= 1

'''if a > 10:
    print("a is greater than 10")
elif a == 10:
    print("a is equal to 10")
else:
    print("a is lesser than 10")'''




















