start_position = 50

class SafeDial:
    def __init__(self, start):
        self.position = start
        self.zero_counter = 0

    def move_left(self, steps):
        self.position = (self.position - steps) % 100
        print(f"Accepted move command: left {steps}")
        print(f"Current position: {self.position}")
        if self.position == 0:
            self.zero_counter += 1
            print(f"Dial hit zero! Total zero hits: {self.zero_counter}")

    def move_right(self, steps):
        self.position = (self.position + steps) % 100
        print(f"Accepted move command: right {steps}")
        print(f"Current position: {self.position}")
        if self.position == 0:
            self.zero_counter += 1
            print(f"Dial hit zero! Total zero hits: {self.zero_counter}")

dial = SafeDial(start_position)

with open ("day1input.txt") as file:
    for line in file:
        command = line[0]
        value = line[1:].strip()
        print(f"Processing command: {command} {value}")
        if command == 'L':
            dial.move_left(int(value))
        elif command == 'R':
            dial.move_right(int(value))
        else:
            print(f"Invalid command: {command}")
    print(f"Final position: {dial.position}")
    print(f"Total times dial hit zero: {dial.zero_counter}")