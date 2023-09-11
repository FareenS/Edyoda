sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def sort_by_last_element(tuple_item):
    return tuple_item[-1]
sorted_list = sorted(sample_list, key=sort_by_last_element)
print(sorted_list)