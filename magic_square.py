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

def main():
    magic_char = choice(ascii_letters)
    magic_square = generate_magic_square(magic_char)
    
main()