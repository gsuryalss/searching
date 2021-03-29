"""
Binary search is used on a collection of sorted items. It relies on the technique of repeatedly dividing the
input into half until it finds the search value.
    * Divide the array element into half & find the median value (//2)
    * check the median element, if it is equal return it
    * if the median element is greater than key, reduce the upper bound to median-1
    * if the median value is lesser than key, increase the lower bound to median+1
As we dispose off one part of the search case during every step of binary search, and perform the search
operation on the other half, this results in a worst case time complexity of O(log2N).
"""


from bubble_sort import bubble_sort


def binary_search(arr_param, item):
    first = 0
    last = len(arr_param) - 1
    found = False

    while first <= last and not found:
        mid_pos = (first + last)//2
        if arr_param[mid_pos] < item:
            first = mid_pos + 1
        elif arr_param[mid_pos] > item:
            last = mid_pos - 1
        else:
            print("Position", mid_pos)
            found = True

    return found


arr = []
print("Binary Search\n")

# array size
m = int(input("Enter the array size:>>"))

# array input
print("Enter the array elements(new line):\n")
for l in range(m):
    arr.append(int(input()))

# input search element
find = int(input("Enter the search value:>>"))

# sort the input array
sorted_arr = bubble_sort(arr)
print("Sorted Array: ", sorted_arr)

# search the element in input array
print("Value Found" if binary_search(sorted_arr, find) else "Value Not Found")
