input_string = input('Which sentence would you like to be reversed?')
split_string =input_string.split()
split_string.reverse()
result = " ".join(split_string)
print(result)