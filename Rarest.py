def nth_most_rare(lst, n):
    # Create a dictionary to store the frequency of each element
    frequency_dict = {}
    for num in lst:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1

    # Create a list of unique elements in the input list
    unique_elements = list(set(lst))

    # Sort the unique elements based on their frequency in ascending order
    sorted_elements = sorted(unique_elements, key=lambda x: (frequency_dict[x], x))

    # If n is out of range, return None
    if n < 1 or n > len(sorted_elements):
        return None

    # Return the nth rarest item
    return sorted_elements[n - 1]

# Example usage:
lst = [5, 4, 5, 4, 5, 4, 4, 5, 3, 3, 3, 2, 2, 1, 5]
n = 2
result = nth_most_rare(lst, n)
print(result)
