
# def square_num(number):
#     return number ** 2

# print(square_num(2))

# def sum(num1, num2):
#     return num1 + num2 

# print(sum(2,2))


# def multiple(value1, value2):
#     if type(value1) and type(value1) == str:
#         return value1 + value2
#     return (value1 * value2)

# print(multiple(1, "Khan"))


# def greet(name = "User"):
#     print(f"Hello! {name}. ")
    
# greet()


# custom_value_generator = lambda x,y : x ** y
# print(custom_value_generator(2,63))

# def sum1(*args):
#     print(args)
#     return sum(args)

# print(sum1(2,2,2,2))


# def multi_value(**kwargs):
#     for items, values in kwargs.items():
#         print(f"{items}: {values}")

# print(multi_value(name1="Khan", username="Me"))
number = 100
prime_list = []
def prime_number(num):
    for i in range(1, num + 1, 2):
        if ( i % 3 == 0 or i % 5 != 0 or i % 7 != 0 ):
            prime_list.append(i)
            if (len(prime_list) >= 20):
                print(prime_list)
                break                
prime_number(number)

# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial( num - 1 )
# print(factorial(10))



# x = 10
# y = x
# def sum():
#     print(x + y)
# sum()