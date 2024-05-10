# Numbers in Python 
# x = 1
# y = 5
# print(x + y)

# x = 4

# x += 5

# print(x)

# x = 5

# y = "Jawad"

# print(x + y) # it throws error

# x = 3 + 5j

# print(x)

# import math

# print(math.pi)

# math.floor

# x = 5

# string_x = str(x)
# float_x = float(x)
# number_x = int(x)
# print(type(string_x))
# print(type(float_x))
# print(type(number_x))


# x = 5
# y = "Jawad"
# print(x**2)
# print(5 * y)


# import math
# import random
# print(math.pi)
# print(random.random())

# pi_value = math.pi

# round_off_pi = round(pi_value, 2)

# print(round_off_pi)
# fruit_list = ["apple", "mango", "banana", "watermelon"]
# random_value = random.randint(0,100)
# random_value = random.randint(fruit_list[0],fruit_list[-1])
# random_value_auto = random.random()

# print(random_value)
# print(random_value_auto)
# print(random.choice(fruit_list))

# my_str = "My Name is Jawad"

# print(my_str[0])
# print(my_str[0:2])
# print(my_str + " Hello")

# print(my_str.upper())
# print(my_str.lower())
# print(my_str.split(" "))

# me = [1,3,4,4]

# print(me.join())

# x = 10

# def sum():
#     x = 15
   
#     def sum2():
#         print(x)
#         y = 10
#     return sum2

# sum()()

# my_set = {1,3,4,5,3,3,4}
# # new_set = my_set and {7,7}
# # print(new_set)
# # print(my_set)

# print(type(my_set))
# my_str = "Jawad Khan"
# slicing_str = my_str[0:]
# print(my_str)
# print(my_str.capitalize()) 
# print(my_str.upper()) 
# print(my_str.lower()) 
# print(my_str.casefold()) 
# print(my_str.find("w"))

# my_str[0] = "H"

# print(my_str)
# my_list = ["Jawad","Khan"]
# print(my_str.split()) # string to list

# print(my_list.join(" "))

# print(my_str[:])

# for char in my_str:
#     print(char)


my_str = "      This is me    or   Jawad      "

# print(my_str.replace("  ", " "))
# print(my_str.strip())

# print(my_str.split(" "))

# print(my_str.count("i"))
# name = "Jawad"
# semester = "5th"
# roll_no = "01003"

# std_info = '''Student Name is {}, {} semester with roll no S24BARIN7M{}.  '''

# print(std_info.format(name, semester, roll_no))
# my_list = ["khan", "Jawad"]
# new_str = "My Name is Khan"

# print(new_str.split(" "))
# print(", ".join(my_list))

# my_str = r"This is \me \n Jawad"
# path = r'c:\user\dotprogrammer '
# print(my_str)
# print(path)
# print("is" in my_str)


# my_list = ["IUB", "Chai-Aur-Python", "Jawad", 12, 19, "End"]

# print(my_list)
# print(my_list[0])
# print(my_list[1])
# my_list[1] = "Chai-Aur-Code"
# print(my_list)
# print(my_list[1])

# my_list.append("Chair aur Jawad")
# my_list.extend(["Khan"])
# my_list.insert(0, "Khan")
# my_list.pop()
# my_list.remove("Jawad")
# print(my_list.index("Chai-Aur-Python"))
# print(my_list)

# for item in my_list:
#     print(item)
# rangeOfList = len(my_list)
# i = 0  
# while ( i < rangeOfList):
#     print(my_list[i])
#     i += 1

# for item in range(0, rangeOfList):
#     print(my_list[item])

# my_list[1:4] = ["Khan", "me", 5]

# new_list = my_list[:]
# new_list.append("Not End")
# new_list.pop()
# new_list.clear()
# new_list.extend(["Me", "Khan"])
# print(new_list)

# print(my_list)

# for items in my_list:
#     print(items)

# list_length = len(my_list)

# for items in range(0, list_length):
#     print(my_list[items])
   
# squared_number = [x**2 for x in range(1,11)] 
# print(squared_number)

# cubed_number = [number ** 3 for number in range (1, 11)]

# print(cubed_number)
# number = int(input("Enter any number: "))
# def even_number(num):
#      return [x ** 1 for x  in range (2, num + 1, 2)]
# result = even_number(number)
# for items in result:
#     print(items)
    
myDict = {
    "username": "Jawad Khan",
    "depart": "AI",
    "roll_no": "01003"
}

# print(myDict)
# print(myDict["username"])

# print(myDict["me"])
# print(myDict.get("roll_no"))
# print(myDict.items())  
# for i, j in myDict.items():
#     print(i, j)



for i in range (1, 15):
    print(i * " *", end= "\n ")
    