def find_highest_frequency_length(string):
    # Split the string into words
    words = string.split()

    # Create a dictionary to store the frequency of each word
    frequency = {}

    # Count the frequency of each word
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    # Find the highest frequency
    max_frequency = max(frequency.values())

    # Find the length of the highest-frequency word
    highest_frequency_length = max(len(word) for word in frequency if frequency[word] == max_frequency)

    return highest_frequency_length


# Test the function with example string
input_string = "The cat jumped over the fence and the dog followed"

result = find_highest_frequency_length(input_string)
print("Length of the highest-frequency word:", result)


# Test Case 1:
input_string_1 = "apple banana apple orange apple banana"
result_1 = find_highest_frequency_length(input_string_1)
print("Length of the highest-frequency word (Test Case 1):", result_1)

# Test Case 2:
input_string_2 = "Hello"
result_2 = find_highest_frequency_length(input_string_2)
print("Length of the highest-frequency word (Test Case 2):", result_2)
