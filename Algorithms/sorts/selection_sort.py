def find_smallest(lst):
    smallest_idx = 0  # 记录最小值的索引
    smallest_val = lst[0]  # 记录最小值

    for i in range(1, len(lst)):
        if smallest_val > lst[i]:
            smallest_idx = i
            smallest_val = lst[i]

    return smallest_idx


def selection_sort(lst):
    arr = []
    for i in range(len(lst)):
        # 找出数组中最小的元素，加入新数组中，并在原数组中删除它
        smallest = find_smallest(lst)
        arr.append(lst.pop(smallest))
    return arr


if __name__ == "__main__":
    my_lst = [5, 3, 6, 2, 10]
    print(selection_sort(my_lst))