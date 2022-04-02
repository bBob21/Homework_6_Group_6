#Exercise 2

list = [1,2,3,4]

def index_nthpower(array, n):
    if(n>len(array)):
        return -1
    else:    
        return array[n]**n

print(index_nthpower(list,2))
