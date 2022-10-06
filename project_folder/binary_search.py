arr = [i for i in range(100)]


# runtime is big O(log n) logarithmic bb
def binary_search(target, array):
    low = 0
    high = len(array)
    mid = (high + low) / 2
    while array[int(mid)] != target:
        if array[int(mid)] > target:
            high = mid
            mid = int(high + low) / 2
        elif array[int(mid)] < target:
            low = mid
            mid = int(high + low) / 2
        print(int(mid))
    return array[int(mid)]

binary_search(37, arr)
