#Task 1
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()  
    merged_dict.update(dict2)   
    return merged_dict

# The function merges two dictionaries into a single dictionary. Time Complexity: (O(n + m)), where n and m are the sizes of the input dictionaries.
# The function creates a new dictionary containing key-value pairs from both input dictionaries. Space Complexity: (O(n + m)).

#Task 2
def intersect_dictionaries(dict1, dict2):
    intersection = {k: dict1[k] for k in dict1 if k in dict2}
    return intersection

# The function finds the intersection of two dictionaries. Time Complexity: (O(n)), where n is the size of the first dictionary.
# The function creates a new dictionary containing key-value pairs that are present in both input dictionaries. Space Complexity: (O(n)).

#Task 3
def count_word_frequencies(word_list):
    frequency_dict = {}
    for word in word_list:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict

# The function counts the frequency of each word in a list. Time Complexity: (O(n)), where n is the number of words in the input list.
# The function creates a new dictionary containing words as keys and their frequencies as values. Space Complexity: (O(n)).
