print("MINEFIELD GENERATOR")
import random

def generate_minefield(rows, cols, num_mines):
    # create a grid with all cells initialized to 0
    minefield = [[0 for _ in range(cols)] for _ in range(rows)]

    # place mines randomly in the grid
    mine_positions = set()
    while len(mine_positions) < num_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if (row, col) not in mine_positions:
            mine_positions.add((row, col))
            minefield[row][col] = 'X'  # place a mine
    
    # calculate numbers for cells adjacent to mines
    for row in range(rows):
        for col in range(cols):
            if minefield[row][col] == 'X':
                continue
            # count adjacent mines
            mine_count = 0
            for r in range(max(0, row - 1), min(rows, row + 2)):
                for c in range(max(0, col - 1), min(cols, col + 2)):
                    if minefield[r][c] == 'X':
                        mine_count += 1
            minefield[row][col] = mine_count

    return minefield

def print_minefield(minefield):
    for row in minefield:
        print(" ".join(str(cell) for cell in row))
    print()

if __name__ == "__main__":
    # example usage
    rows = 5
    cols = 5
    num_mines = 3

    minefield = generate_minefield(rows, cols, num_mines)
    print_minefield(minefield)