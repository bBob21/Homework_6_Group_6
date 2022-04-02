# Exercise 5

def backward_string_by_word(text: str):
    result = ' '.join([x[::-1] for x in text.split(' ')])
    return result


if __name__ == '__main__':
    print("Hello World")
    print(backward_string_by_word('Hello World'))
