total = 0

def validate_input(lower, upper):
    nums_to_add = 0
    for value in range(lower, upper + 1):
        print(f"Checking value: {value}")
        str_value = str(value)
        result = sum_strings_with_repeated_substrings([str_value])
        nums_to_add += result
            
    print(f"Sum of valid numbers between {lower} and {upper}: {nums_to_add}")
    return nums_to_add

def sum_strings_with_repeated_substrings(strings):
    total = 0
    for s in strings:
        if has_repeated_substring(s):
            print(f"  Valid number found: {s}")
            total += int(s)
    return total

def has_repeated_substring(s):
    return s in (s + s)[1:-1]

with open("day2input.txt") as file:
    for line in file:
        parts = line.strip().split(',')
        for part in parts:
            bounds = part.split('-')
            lower = int(bounds[0])
            upper = int(bounds[1])
            total += validate_input(lower, upper)
    
print(f"Total sum of valid numbers: {total}")