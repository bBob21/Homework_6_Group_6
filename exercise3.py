#Exercise 3

list = [1,2,3,4,5]

def remove_all_after(array,number):
    #pre define variable
    index = 0

    #check each elements in the array
    for x in array:
        index += 1
        
        if x == number:
            break

    #return items until the number
    return array[0:index]

print(remove_all_after(list,3))