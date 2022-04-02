# Exercise 5

print("Howdy")
def backward_string_by_word(text: str):
    result = ' '.join([x[::-1] for x in text.split(' ')])
    return result


if __name__ == '__main__':
    print("howdy")
    print(backward_string_by_word('howdy'))
