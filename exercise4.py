#Exercise 4

given_list = [5,4,7,3,4,5,4]

def chunking_by(array,number):
    #predefine chunked list
    chunks = []

    #for every number between 0 to the length of the list
    #at intervals of the given number
    #example: range(0,10,2) = 0,2,4,6,8,10
    #example: range(0,15,4) = 0,4,8,12
    for a in range(0,len(array),number):

        #add sections of the original list into the new chunks list
        #to create a 2d array
        chunks.append(array[a:a+number])

    return chunks

print(list(chunking_by(given_list,3)))