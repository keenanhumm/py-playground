import sys


def convert_to_list(num_string):
    raw_nums = num_string.split(',')
    for i in range(len(raw_nums)):
        raw_nums[i] = int(raw_nums[i].strip())
    return raw_nums


def get_second_smallest(list_nums):
    smallest = sys.maxsize
    sec_smallest = sys.maxsize
    for i in range(len(list_nums)):
        if list_nums[i] < smallest:
            sec_smallest = smallest
            smallest = list_nums[i]
        elif list_nums[i] < sec_smallest:
            sec_smallest = list_nums[i]
    return sec_smallest


# get list
num_list = input("Provide comma separated list of numbers:\n")

# process list
resultant_list = convert_to_list(num_list)
second_smallest = get_second_smallest(resultant_list)

# print result
print(f"The second smallest in your list is {second_smallest}")