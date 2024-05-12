


# def auth(func):
#     def wrapper(*args, **kwargs):
#         if kwargs:
#             if kwargs["name"] != "Jawad":
#                 return print("Oops!! Sorry you are not authorized ")
#             print("You are Authorized")
#         return func(*args, **kwargs)

#     return wrapper
# @auth
# def sum(a,b, name = ""):
#     print(f"The sum of {a} and {b} is {a+b}")
    
# sum(2,5, name = "Khan")



# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         total_time = end_time - start_time
#         print(f"The function ran in {total_time}")
#         return result
#     return wrapper
# @timer
# def calculate_time(a, b):
#     time.sleep(2)
#     print(a + b)

# calculate_time(5, 10)




# def arguments_checker(func):
#     def wrapper(*args, **kwargs):
#         args_value = (", ".join(str(arg) for arg in args))
#         kwargs_value = (", ".join(f"{k}: {v}" for k, v in kwargs.items()))
#         print(f" {func.__name__} The args value : {args_value} and kwargs[    {kwargs_value}]  ")
#         result = func(*args, **kwargs)
#         return result
#     return wrapper
# @arguments_checker
# def calculate_time(a, b, name = "Jawad"):
#     print(a + b, name)

# calculate_time(5, 10, name= "Khan")

import time

def cache(func):
    def wrapper(*args, **kwargs):
        cache_value = {}
        
        print(cache_value)
        if args in cache_value:
            cache_value.setdefault("args", args)
            print(cache_value["args"])
            return cache_value["args"]
        return func(*args, **kwargs)
    return wrapper
        
@cache       
def sum(a,b):
    time.sleep(1)
    print(a + b)
sum(4, 10)
sum(4, 10)
    