def find_highest_voltage(battery_bank):
    battery_bank = str(battery_bank)
    best_value = 0
    best_first_index = -1
    best_second_index = -1
    best_first_digit = 0
    best_second_digit = 0
    
    for i in range(len(battery_bank)):
        first_digit = int(battery_bank[i])
        for j in range(i + 1, len(battery_bank)):
            second_digit = int(battery_bank[j])
            pair_value = first_digit * 10 + second_digit
            if pair_value > best_value:
                best_value = pair_value
                best_first_index = i
                best_second_index = j
                best_first_digit = first_digit
                best_second_digit = second_digit
    
    print(f"  First digit: {best_first_digit} at position {best_first_index}")
    print(f"  Second digit: {best_second_digit} at position {best_second_index}")
    print(f"  Position check: second position ({best_second_index}) > first position ({best_first_index})? {best_second_index > best_first_index}")
    print(f"  Two-digit value: {best_value}")
    
    return best_first_digit, best_second_digit

with open("day3input.txt") as file:
    total = 0
    for line in file:
        battery_bank = line.strip()
        first, second = find_highest_voltage(battery_bank)
        value = f"{first}{second}"
        total += int(value)
        print(f"Best voltage combination: {value}")
    print(f"Total sum of best voltage combinations: {total}")