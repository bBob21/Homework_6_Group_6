# Exercise 5

def backward_string_by_word(text: str):
    
    result = ' '.join([x[::-1] for x in text.split(' ')])
    
    # explanation:
        # for x in text.split(' '):
            # takes the string input and converts it into a list using .split(' ')
            # then make a for loop with x as the elements of the list
        # ' '.join([x[::-1]]):
            # x[::-1] means look at the letters in x backwards
            # if x = Hello, it would look like olleH
            # and combines each reversed word with a space using ' '.join()
            
    return result


if __name__ == '__main__':
    print("Hello World")
    print(backward_string_by_word('Hello World'))
