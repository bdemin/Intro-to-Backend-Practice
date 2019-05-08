def rot13(string):
    # rot13 takes a string as input and returns the same
    # string with each character advanced by 13
    # rot13('hello') -> 'uryyb'
    # rot13('HELLO') -> 'URYYB'

    new_str = ''
    for char in string:
        temp = ord(char)
        if char.islower():
            temp += 13
            if temp > 122:
                temp -= 26
        else:
            temp += 13
            if temp > 90:
                temp -= 26
        new_str += chr(temp)
    return new_str


# print(rot13('abc'))
# print(rot13('ABC'))
# print(rot13('xyz'))
# print(rot13('WXY'))
# print(rot13('hello'))