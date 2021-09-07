'''Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.
// Returns i
Hints: Use if/elif to deal with conditions.'''

import math
def binary_search(list1,element):
    lower_bound = 0
    upper_bound = len(list1)-1
    index = -1
    while upper_bound>=lower_bound and index == -1:
        mid = int(math.floor(upper_bound+lower_bound)/2.0)
        if list1[mid]==element:
            index = mid
        elif list1[mid] > element:
            upper_bound = upper_bound-1
        else:
            lower_bound = lower_bound + 1
    return index

list1=[2,5,7,9,11,17,222]
print binary_search(list1,11)
print binary_search(list1,222)

