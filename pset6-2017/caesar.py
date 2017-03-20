import cs50
import sys

# Caesar is a program that will take a command line argument from the user as
# a "key", a non-negative integer, that will be used to encode a string of text 
# provided by the user. The program will preserve case of alphabetic characters
# and will not encode any non-alphabetical characters.

def main():
    # Quit program if user does not provide the right number of command line args.
    if len(sys.argv) != 2:
        print("Usage: python caesar.py <key>")
        exit(1)
    
    # As values for argv[] are stored as strings, we will convert the string to an int.
    key = int(sys.argv[1])
    
    print("plaintext: ", end="")
    text = cs50.get_string()
    
    if text != None:
        print("ciphertext: ", end="")
        # We will loop through each character in the user-provided string, ciphering
        # each alphabetic character and just printing any other type of character.
        for c in text:
            if c.isalpha():
                if c.isupper():
                    print(chr((ord(c) - ord('A') + key) % 26 + ord('A')), end="")
                else:
                    print(chr((ord(c) - ord('a') + key) % 26 + ord('a')), end="")
            else:
                print(c, end="")
        print()
        exit(0)

# cipher is the function that will take an alphabetical character as an argument.
# It will output the encrypted result when that character is rotated by the 
# correct number of positions in the user-provided "key". Cipher uses an if statement
# to check the case of the letter and applies the correct algorithm in order to
# preserve case. 

'''
def cipher(letter, key):
    if letter.isupper:
        return chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
    else:
        return chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
'''

if __name__ == "__main__":
    main()