def uniq_add(my_list=[]):
    sorted_list = my_list.copy()
    sorted_list.sort()
    unique = [sorted_list[i] for i in range(len(sorted_list))
              if i == 0 or sorted_list[i] != sorted_list[i - 1]]
    result = sum(unique)
    return (result)
