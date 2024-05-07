# me = 1
# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#          yield i

# print(even_generator(10))


def even_numbers(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2

# Example usage:
limit = 20
for even_num in even_numbers(limit):
    print(even_num)
