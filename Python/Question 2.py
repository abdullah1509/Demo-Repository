def is_valid_string(string):
    # Count the frequency of each character
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    # Count the frequency of frequencies
    freq_count = {}
    for count in char_count.values():
        freq_count[count] = freq_count.get(count, 0) + 1

    # If all characters have the same frequency, it is a valid string
    if len(freq_count) == 1:
        return "YES"

    # If there are exactly two frequencies
    elif len(freq_count) == 2:
        # If one frequency occurs only once and its count is 1
        if freq_count.get(1, 0) == 1:
            return "YES"
        # If the difference between the two frequencies is 1 and the higher frequency occurs only once
        max_freq = max(freq_count)
        min_freq = min(freq_count)
        if freq_count[max_freq] == 1 and max_freq - min_freq == 1:
            return "YES"

    # The string is not valid according to the conditions
    return "NO"


# Test the function with example string
input_string = "aabbcc"
result = is_valid_string(input_string)
print(result)

# Test Case 1:
input_string_1 = "aaaaaa"
result_1 = is_valid_string(input_string_1)
print("Result for Test Case 1:", result_1)

# Test Case 2:
input_string_2 = "aabbcccc"
result_2 = is_valid_string(input_string_2)
print("Result for Test Case 2:", result_2)
