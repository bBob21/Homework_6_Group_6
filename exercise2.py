#Exercise 2
def index_nthpower(array, n):
    if(n>len(array)):
        return -1
    else:    
        return array[n]**n
