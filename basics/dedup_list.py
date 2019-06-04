my_nums = [4, 2, 3, 3, 4, 5, 5, 1, 2]


def dedup_list(num_list):
    no_dup = []
    for x in num_list:
        if x not in no_dup:
            no_dup.append(x)
    no_dup.sort()
    return no_dup


print(dedup_list(my_nums))
