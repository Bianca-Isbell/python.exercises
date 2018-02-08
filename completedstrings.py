# Strings Exercise 1: Uppercase a String
s = ("this is a string. is it upper or lower case?").upper()
print(s)

# Strings Exercise 2: Capitalize a String
s = ("this is a string. Is it upper or lower case?").capitalize()
print(s)

# Strings Exercise 3: Reverse a String
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

s = "Geeksforgeeks"

print ("The original string  is : ",end="")
print (s)

print ("The reversed string(using loops) is : ",end="")
print (reverse(s))

# Strings Exercise 4: Leetspeak
word = input('The word: ').upper()

# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7

word = word.replace('A', '4')
word = word.replace('E', '3')
word = word.replace('G', '6')
word = word.replace('I', '1')
word = word.replace('O', '0')
word = word.replace('S', '5')
word = word.replace('T', '7')

print(word)

# Strings Exercise 5: Long-long Vowels
word = 'cheese'
word2 = 'Good'
word3 = 'Man'
word4 = 'Spoon'

word = word.replace('ee', 'eeeee')
word2 = word2.replace('oo', 'ooooo')
word4 = word4.replace('oo', 'ooooo')

print(word)
print(word2)
print(word3)
print(word4)

# Strings Exercise 6: Caesar Cipher
secret = "Lbh zhfg hayrnea, jung lbh unir yrnearq."
offset = 13
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = ''

for char in secret:
    ascii_code = ord(char)
    is_uppercase = ascii_code >= 65 and ascii_code <= 90
    char = char.lower()
    if char not in alphabet:
        new_char = char
    else:
        idx = alphabet.find(char)
        new_idx = idx + offset
        if new_idx > 25:
            new_idx = new_idx - 26
        new_char = alphabet[new_idx]
        if is_uppercase:
            new_char = new_char.upper()
    result += new_char

print(result)