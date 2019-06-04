import sys

smallest = -sys.maxsize
sec_smallest = -sys.maxsize

# get list
num_list = input("Provide comma separated list of numbers:\n")

# process list
resultant_list = convert_to_list(num_list)
second_smallest = get_second_smallest(resultant_list)

# print result
print(f"The second smallest in your list is {second_smallest}")
