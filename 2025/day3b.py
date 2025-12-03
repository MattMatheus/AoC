def find_highest_voltage(battery_bank, num_batteries=12):
    battery_bank = str(battery_bank)
    n = len(battery_bank)
    
    if n < num_batteries:
        return None
    
    result = []
    start_pos = 0
    
    for pos in range(num_batteries):
        remaining_needed = num_batteries - pos - 1
        search_end = n - remaining_needed
        best_digit = -1
        best_index = -1
        
        for i in range(start_pos, search_end):
            digit = int(battery_bank[i])
            if digit > best_digit:
                best_digit = digit
                best_index = i
        
        result.append(best_digit)
        start_pos = best_index + 1
        
        print(f"  Position {pos}: selected digit {best_digit} from index {best_index}")
    
    return ''.join(map(str, result))

with open("day3input.txt") as file:
    total = 0
    for line_num, line in enumerate(file, 1):
        battery_bank = line.strip()
        print(f"\nProcessing bank {line_num}: {battery_bank}")
        voltage = find_highest_voltage(battery_bank, 12)
        if voltage:
            print(f"  Best voltage: {voltage}")
            total += int(voltage)
        else:
            print(f"  Error: Not enough batteries in bank")
    
    print(f"\nTotal sum of best voltage combinations: {total}")
