# age = 20
# if age < 13:
#     print("Child")

# elif age <= 19:
#     print("Teen Ager")

# elif age <= 59:
#     print("Adult")

# else:
#     print("Senior")
    
# day = "Wednesday"
# age = 100
# if day == "Wednesday" and age < 18:
#     print("It's Wednesday so discount is $2 for Children and price is $6")

# elif day != "Wednesday" and age < 18:
#     print("It's not Wednesday so no discount and price is $8 for children")
# elif day == "Wednesday" and age >= 18:
#     print("It's Wednesday so discount is $2 for Adult and price is $10")

# elif day != "Wednesday" and age >= 18:
#     print("It's not Wednesday so no discount and price is $12 for Adult")
    
# year = 1996

# if year % 4 == 0:
#     print(year, "is leap year")
# else :
#     print(year, "Not a leap year")


# number = 10

# for i in range (1, number + 1):
#     print("Hello World!", i)

# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# postive_number = 0 

# for item in numbers:
#     if item > 0:
#         postive_number += 1
# print(postive_number)

# user_number = 4

# sum_numbers = 0

# for i in range (1, user_number+1):
#     if i % 2 == 0:
#         sum_numbers += i
# print(sum_numbers)

# number = 10

# for i in range (1, 11):
#     if i == 5:
#         continue
#     print(f"{i} X {number} = {i*number}")

# string = "Python"
# index = len(string)
# reversed_str = ""
# for i in string:
#     reversed_str = reversed_str + string[index-1]
#     index -= 1
# print(reversed_str)
# input_str = "Python"
# reversed_str = ""

# for char in input_str:
#     reversed_str = char + reversed_str  

# print(reversed_str)


# string = "jwwwawaaaaaaaddddddd"
# count = 0
# for char in string:
   
#     if string.count(char) != 1:
#         print("Character is ", char)
#         break

# number = 1

# factorial = 1

# for i in range (1, number + 1):
#     if number == 0 or number == 1:
#         factorial = 1
#     else:
#          factorial *= i
# print(factorial) 

# while True:
#     number = int(input("Enter a number between 1 to 10: "))
#     if 1 < number < 11:
#         print("Enjoy")
#         break
#     else:
#         print("Oops! invalid please try again")

items = [ "mango", "apple", "mango", "banana", "orange", "apple", "mango"]
# duplicate = []
# for item in items:
#     print(items.count([item]))
#     # if items.count[item] > 1:
#     #     items.append(item)
#     #     break
    
# print(duplicate)

# for item in range (0, len(items)):
#     if items.count(items[item]) > 1:
#         duplicate.append(items[item])
#         break 
# print(duplicate)

# iteration = iter(items)

# print(iteration.__next__(), iteration.__next__(), iteration.__next__(), iteration.__next__())
# print(next(iteration))