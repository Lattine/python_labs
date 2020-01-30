def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]  # 取数组第一个元素作为基准值
        less = [i for i in lst[1:] if i <= pivot]  # 所有小于等于基准值的元素构成子数组
        greater = [i for i in lst[1:] if i > pivot]  # 所有大于基准值元素构成的子数组
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    my_lst = [5, 3, 6, 2, 10]
    print(quick_sort(my_lst))