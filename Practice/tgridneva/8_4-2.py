def filter_strings(strings):
    return [s for s in strings if len(s) >= 5]


input_strings = ['hello', 'i', 'write', 'cool', 'code']
result = filter_strings(input_strings)
print(result)
