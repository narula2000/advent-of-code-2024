from os import getpriority


data = []
with open("input.txt", "r") as file:
    for line in file:
        data.append([char for char in line.strip()])

out = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
    "..........",
]

test = [[char for char in row] for row in out]
print(test)


def search2D(grid, row, col, word):
    m = len(grid)
    n = len(grid[0])

    if grid[row][col] != word[1]:
        return 0

    x = [-1, -1, 1, 1]
    y = [-1, 1, -1, 1]

    for dir in range(4):
        # Initialize starting point for current direction
        currX, currY = row + x[dir], col + y[dir]

        # break if out of bounds
        if currX >= m or currX < 0 or currY >= n or currY < 0:
            return 0

        # Moving in particular direction
        currX += x[dir]
        currY += y[dir]

    top_left = grid[row - 1][col - 1]
    top_right = grid[row - 1][col + 1]
    bottom_left = grid[row + 1][col - 1]
    bottom_right = grid[row + 1][col + 1]
    if top_right == top_left and bottom_right == bottom_left:
        if (top_right == "M" and bottom_left == "S") or (
            top_right == "S" and bottom_left == "M"
        ):
            return 1
    if top_left == bottom_left and top_right == bottom_right:
        if (top_right == "M" and top_left == "S") or (
            top_right == "S" and top_left == "M"
        ):
            return 1

    # if word is not found in any direction,
    # then return false
    return 0


# This function calls search2D for each coordinate
def searchWord(grid, word):
    m = len(grid)
    n = len(grid[0])

    ans = 0

    for i in range(m):
        for j in range(n):
            # if the word is found from this coordinate,
            # then append it to result.
            ans += search2D(grid, i, j, word)

    return ans


print("Test Ans:", searchWord(test, "MAS"))
print("Input Ans:", searchWord(data, "MAS"))
