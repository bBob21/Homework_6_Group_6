#Exercise 1

list = [1, 2, 3, 4]

def replace_last(list):
    return list[-1:] + list[:-1]

print(replace_last(list))
