import sys


def longest_unique_substring(user_string=''):
    i = 0
    max_length = -sys.maxsize
    while i < len(user_string):
        used_chars = dict()
        j = i
        while j < len(user_string) and (user_string[j] not in used_chars):
            used_chars[user_string[j]] = True
            j += 1
        max_length = max(max_length, j-i)
        i = j

    return max_length


user_input = input("Provide a string: ")
print(f"The longest string of unique characters in '{user_input}' is {longest_unique_substring(user_input)} characters long.")
