first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [word for word in first_strings if len(word) >= 5]
print(first_result)

second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]
print(second_result)

overall_strings = first_strings + second_strings
third_result = {word: len(word) for word in overall_strings if len(word) % 2 == 0}
print(third_result)
