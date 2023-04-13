import sys
import random
import time


def translate():
    dictionary = {}
    with open("dictionary.txt") as f:
        for line in f:
            (key, val) = line.split()
            dictionary[str(key)] = int(val)
    dictionary[" "] = 36  
    return dictionary

def encode(message):
    # Convert extra characters to spaces
    message = message.replace('\n', ' ').replace('\t', ' ')

    # Get dectionary values
    dict = translate();

    # Group the plaintext into sets of five characters per group
    message = message.ljust((len(message) + 4) // 5 * 5, ' ')
    groups = [message[i:i+5] for i in range(0, len(message), 5)]


    # Convert each group into a separate number
    numbers = []
    for group in groups:
        num = 0
        for i, c in enumerate(group):
            num += dict[c] * (37 ** (4 - i))
        numbers.append(num)
    # return encoded_message
    return numbers


def decode(encoded_message):
    
    # Get dectionary values
    dict = translate();
    key_list = list(dict.keys())
    val_list = list(dict.values())
    
    # Convert each number to its character grouping
    groups = []
    for num in encoded_message:
        group = ''
        for i in range(5):
            char_code = num % 37
            position = val_list.index(char_code)
            c = key_list[position]
            if c == '\x00':
                c = ' '
            group = c + group
            num //= 37
        groups.append(group)

    # Concatenate the resulting groups to form the decoded message
    decoded_message = ''.join(groups)

    return decoded_message






