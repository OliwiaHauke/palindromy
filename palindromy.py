def palindrom(word):
    return word == word[::-1]
"""
Checks if the given word is a palindrom.

Parameter:
word(str): the word to check

Returns:
bool: True if the word is a palindrome, False otherwise.

"""

print(palindrom("potop"))
print(palindrom("krowa"))
print(palindrom("kajak"))
print(palindrom("zaraz"))
print(palindrom("potop"))
