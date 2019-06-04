import sys

input_string = input("Provide a comma-separated list of integers: ")

input_list = input_string.split(',')
integer_list = [int(x.strip()) for x in input_list]

max_element = sys.maxsize * -1

for num in integer_list:
    if num > max_element:
        max_element = num

print(f"The largest integer in that list is {max_element}.")