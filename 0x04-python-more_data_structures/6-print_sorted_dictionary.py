def print_sorted_dictionary(a_dictionary):
    sort_d = sorted(a_dictionary.items())
    for key, value in sort_d:
        print(f"{key}: {value}")
