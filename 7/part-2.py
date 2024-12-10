data = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        rows = line.split(":")
        vals = rows[1].split()
        data.append((int(rows[0]), [int(val) for val in vals]))

t_data = []
with open("test.txt", "r") as file:
    for line in file:
        line = line.strip()
        rows = line.split(":")
        vals = rows[1].split()
        t_data.append((int(rows[0]), [int(val) for val in vals]))


def permute_operations(numbers):
    def helper(index, current_value):
        if index == len(numbers):  # Base case: all numbers processed
            results.append(current_value)
            return
        # Add
        helper(index + 1, int(current_value) + int(numbers[index]))
        # Multiply
        helper(index + 1, int(current_value) * int(numbers[index]))
        # Concatenate
        helper(index + 1, int(str(current_value) + str(numbers[index])))

    if not numbers:
        return []

    results = []
    # Start recursion with the first number
    helper(1, numbers[0])
    return results


ans = 0
for res, vals in t_data:
    potential_res = permute_operations(vals)
    if res in potential_res:
        ans += res

print(ans)

ans = 0
for res, vals in data:
    potential_res = permute_operations(vals)
    if res in potential_res:
        ans += res

print(ans)
