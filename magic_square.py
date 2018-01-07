from random import choice
from string import ascii_letters, ascii_lowercase, ascii_uppercase

def generate_magic_square(magic_char):
    magic_square = []
    for i in range(100):
        if i % 9 == 0:
            magic_square.append(magic_char)
        elif i % 2 == 0:
            magic_square.append(choice(ascii_uppercase))
        else:
            magic_square.append(choice(ascii_lowercase))
    return magic_square

def print_headers():
    header = '''\
Program #1: Russian Magic Square
Author: Vittoria Laudando
Date: January 7, 2018
System: Visual Studio Code on OSX
    '''
    print(header)

def print_magic_square(magic_square):
    for i in range(99, -1, -1):
        if i % 10 == 0:
            print('{}: {}'.format(i, magic_square[i]))
        else:
            print('{}: {}'.format(i, magic_square[i]), end=' ')
    print()

def print_instructions():
    instructions = '''\
1. Choose any two-digit number in the table above (e.g. 73).
2. Subtract its two digits from itself (e.g. 73 - 7 - 3 = 63)
3. Find this new number (e.g. 63) and remember the letter next to it.
4. Now press the return key and I'll read your mind...
    '''
    print(instructions)

def main():
    magic_char = choice(ascii_letters)
    magic_square = generate_magic_square(magic_char)
    print_headers()
    print_magic_square(magic_square)
    print_instructions()
    input()
    print('You selected the character: ', magic_char)
    
main()