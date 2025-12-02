class SmartSafeDial:
    def __init__(self, num_positions=100, starting_position=50):
        self.num_positions = num_positions
        self.cumulative_rotation = starting_position
    
    def turn_right(self, steps):
        """Turn right, return final position and times 0 was crossed"""
        old_rotation = self.cumulative_rotation
        self.cumulative_rotation += steps
        times_crossed = self.cumulative_rotation // self.num_positions - old_rotation // self.num_positions
        
        position = self.cumulative_rotation % self.num_positions
        return position, times_crossed
    
    def turn_left(self, steps):
        """Turn left, return final position and times 0 was crossed"""
        old_rotation = self.cumulative_rotation
        self.cumulative_rotation -= steps

        # For left turns, use ceiling division: -(-x // n) computes ceil(x/n)
        # This correctly counts when we land exactly on 0
        times_crossed = -(-old_rotation // self.num_positions) - (-(-self.cumulative_rotation // self.num_positions))

        position = self.cumulative_rotation % self.num_positions
        return position, times_crossed
    
    @property
    def position(self):
        return self.cumulative_rotation % self.num_positions

dial = SmartSafeDial(num_positions=100, starting_position=50)

with open ("day1input.txt") as file:
    total_zero_crosses = 0
    
    for line in file:
        command = line[0]
        value = line[1:].strip()
        print(f"Processing command: {command} {value}")
        
        if command == 'L':
            position, crosses = dial.turn_left(int(value))
        elif command == 'R':
            position, crosses = dial.turn_right(int(value))
        else:
            print(f"Invalid command: {command}")
            continue
        
        total_zero_crosses += crosses
        print(f"  Position: {position}, Crossed 0: {crosses} times")
    
    print(f"Final position: {dial.position}")
    print(f"Total times dial hit zero: {total_zero_crosses}")