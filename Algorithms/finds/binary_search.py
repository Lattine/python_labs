def binary_search(lst, key):
    # lst   : 正序列表
    # item  : 需要查找的元素
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]
        if guess == key:
            return mid
        if guess > key:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":
    my_lst = [1, 3, 5, 7, 9]
    print(binary_search(my_lst, 3))
    print(binary_search(my_lst, 8))