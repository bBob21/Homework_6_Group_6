#Exercise 4

list = [1,2,3,4,5]

def remove_all_after(array,number):
    print(f"hi{array}")
    #check each elements in the array
    for element in array:

        while element == number:
            array.pop()

    return array

print(remove_all_after(list,3))
