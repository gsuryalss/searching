"""
Linear search is used on a collections of items. It relies on the technique of traversing a list from
start to end by exploring properties of all the elements that are found on the way.

The time complexity of the linear search is O(N) because each element in an array is compared only once.
"""


def linear_search(arr_param, item):
    pos = 0
    found = False

    while pos < len(arr_param) and not found:
        if arr_param[pos] == item:
            found = True
            print("Position", pos)
        else:
            pos += 1

    return found


arr = []
print("Linear Search\n")

# array size
m = int(input("Enter the array size:>>"))

# array input
print("Enter the array elements(new line):\n")
for l in range(m):
    arr.append(int(input()))

# input search element
find = int(input("Enter the search value:>>"))

# search the element in input array
print("Value Found" if linear_search(arr, find) else "Value Not Found")
