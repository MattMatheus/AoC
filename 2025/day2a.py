def validate_input(lower, upper):
    nums_to_check = set(range(lower, upper + 1))
    nums_to_add = 0
    for value in nums_to_check:
        print(f"Checking value: {value}")
        str_value = str(value)
        mid = len(str_value) // 2
        first_half = str_value[:mid]
        second_half = str_value[mid:]
        if first_half == second_half:
            nums_to_add += value
            print(f"  Valid number found: {value}")
    print(f"Sum of valid numbers between {lower} and {upper}: {nums_to_add}")
    return nums_to_add

total = 0

with open("day2input.txt") as file:
    for line in file:
        parts = line.strip().split(',')
        for part in parts:
            bounds = part.split('-')
            lower = int(bounds[0])
            upper = int(bounds[1])
            total += validate_input(lower, upper)
    

print(f"Total sum of valid numbers: {total}")