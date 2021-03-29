"""
Ternary search is used on a collection of sorted items. It relies on the technique of repeatedly dividing the
input into 1/3 until it finds the search value.
    * Divide the array element into 1/3 & find the median value (//3)
    * check the median element, if it is equal return it
    * if the median element is greater than key, reduce the upper bound to median-1
    * if the median value is lesser than key, increase the lower bound to median+1

Worst case time complexity of O(log3N).
"""


from bubble_sort import bubble_sort


def ternary_search(arr_param, item):
    first = 0
    last = len(arr_param) - 1
    found = False

    while first <= last and not found:
        mid_pos1 = first + (last - 1)//3
        mid_pos2 = last - (last-1)//3

        if arr_param[mid_pos1] == item:
            pos = mid_pos1
            found = True
        elif arr_param[mid_pos2] == item:
            pos = mid_pos2
            found = True
        elif item < arr_param[mid_pos1]:
            last = mid_pos1 - 1
        elif item > arr_param[mid_pos2]:
            first = mid_pos2 + 1
        else:
            first, last = mid_pos1+1, mid_pos2-1

    print("Position: ", pos)
    return found


arr = []
print("Ternary Search\n")

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
print("Value Found" if ternary_search(sorted_arr, find) else "Value Not Found")