#Task 1
def squares_list(n):
    return [i**2 for i in range(1, n+1)]

# The function iterates over numbers from 1 to (n), performing a constant-time operation (squaring a number) for each element. Time Complexity: (O(n)).
# The function creates a new list containing (n) elements, each being a square of an integer. Space Complexity: (O(n)).

#Task 2
def reverse_sublist(lst, i, j):
    lst[i:j+1] = lst[i:j+1][::-1]
    return lst

# The function reverses a sublist of a given list in-place. Time Complexity: (O(j - i)), where i and j are the start and end indices of the sublist.
# The function modifies the input list in-place, without creating a new list. Space Complexity: (O(1)).

#Task 3
def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

# The function merges two sorted lists into a single sorted list. Time Complexity: (O(n + m)), where n and m are the lengths of the input lists.
# The function creates a new list containing elements from both input lists. Space Complexity: (O(n + m)).

