# x = 10

# y = x

# x = 20 

# print(x)
# print(y)


#  Data Types in Python

# Number 
# x = 5
# y = str(x)
# z = 5.092
# print(type(x))
# print(type(y))
# print(type(z))

# x = "Jawad Khan"

# print(x)
# print(type(x))

# list = ["Jawad Khan", True, False, 53, None]
# list.append("IUB")
# list.insert(3, "Khan")
# print(list[:])

# myDic = {
#     "username": "Jawad Khan",
#     "password": "Khan12"
# }
# myDic["username"] = "Khan"
# print(myDic["username"])

# import math
# import random
# print(math.pi)
# print(random.random())

# myTuple = ("C", "M", "D")
# print(random.choice(myTuple))

# username = "Jawad Khan"
# username[8] = "me" 
# print(username[0:5])
# print(username[-8])
# print(dir(username))
# print(len(username))

# myList = ["Jawad Khan", "It's me", True, False, ["This is another"]]

# print((myList[4][0]))


# myDict = {
#     "Name": "Jawad",
#     "Roll": "S22RPHYS1M01025",
#     "Department": "Physics and AI"
# }

# print(myDict["Name"], myDict["Department"], myDict["Roll"])

# myTuple = ("Jawad Khan", "This is me")
# print(myTuple[1])

# myList = None
# myDict = {}
# print(myList, myDict)


# import sys

# print(sys.getrefcount("Jawad"))
# print(sys.getrefcount(2345343))
# print(sys.getrefcount(1))


# myListOne = [1,2,3]

# myListTwo = myListOne

# myListOne = [43,3]
# print(myListOne)
# print(myListTwo)

# n = [1,2,3]
# m = n
# m = [45,5]
# print(n)
# print(m)

# z = [1,2,3]
# x = [4,5,4]
# z[0] = 34
# print(z)
# print(x)

# i = [1,2,3]
# j = i[:]
# i[0] = 44
# print(i)
# print(j)


# import copy

# j = [1,3,5, [45,34, [45]]]
# i = copy.copy(j)
# print(i)

a = [1,43]
b = a

c = [1,43]
d = [1,43]
print( a is b)
print(c is d)

