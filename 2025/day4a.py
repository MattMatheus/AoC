with open("day4input.txt") as file:
    paper_grid = [list(line) for line in file.read().splitlines()]

def count_adjacent_paper_rolls(paper_grid, current_row, current_col):
    adjacent_roll_count = 0
    for row_offset in [-1, 0, 1]:
        for col_offset in [-1, 0, 1]:
            if row_offset == 0 and col_offset == 0:
                continue
            
            neighbor_row = current_row + row_offset
            neighbor_col = current_col + col_offset
            if 0 <= neighbor_row < len(paper_grid) and 0 <= neighbor_col < len(paper_grid[0]):
                if paper_grid[neighbor_row][neighbor_col] == '@':
                    adjacent_roll_count += 1
    
    return adjacent_roll_count

accessible_roll_count = 0

for row_index in range(len(paper_grid)):
    for col_index in range(len(paper_grid[0])):
        if paper_grid[row_index][col_index] == '@':
            adjacent_count = count_adjacent_paper_rolls(paper_grid, row_index, col_index)
            if adjacent_count < 4:
                accessible_roll_count += 1

print(f"Accessible rolls: {accessible_roll_count}")