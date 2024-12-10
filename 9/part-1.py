data = ""
with open("input.txt", "r") as file:
    for line in file:
        data = line.strip()

t_data = ""
with open("test.txt", "r") as file:
    for line in file:
        t_data = line.strip()

DELIMITER_STR = chr(1114110)
DELIMITER_INT = ord(DELIMITER_STR)


idx_uid = -1
disk = ""
for idx in range(0, len(t_data), 2):
    idx_uid += 1
    uid = chr(idx_uid)
    window = t_data[idx : idx + 2]
    if len(window) == 2:
        file, space = window[0], window[1]
        frag = f"{uid*int(file)}{DELIMITER_STR*int(space)}"
        disk += frag
    elif len(window) == 1:
        frag = f"{uid*int(window[0])}"
        disk += frag


# SWAP
disk = list(disk)
left = 0
right = len(disk) - 1
while left <= right:
    # Move the left pointer until it points to a non-DELIMITER_STR element
    while left < len(disk) and disk[left] != DELIMITER_STR:
        left += 1

    # Move the right pointer until it points to a DELIMITER_STR element
    while right >= 0 and disk[right] == DELIMITER_STR:
        right -= 1

    # If left is less than or equal to right, swap the values
    if left <= right:
        disk[left], disk[right] = disk[right], disk[left]
        left += 1
        right -= 1

ans = 0
for i, char in enumerate(disk):
    if char != DELIMITER_STR:
        ans += i * ord(char)

print(ans)

idx_uid = -1
disk = ""
for idx in range(0, len(data), 2):
    idx_uid += 1
    uid = chr(idx_uid)
    window = data[idx : idx + 2]
    if len(window) == 2:
        file, space = window[0], window[1]
        frag = f"{uid*int(file)}{DELIMITER_STR*int(space)}"
        disk += frag
    elif len(window) == 1:
        frag = f"{uid*int(window[0])}"
        disk += frag

# SWAP
disk = list(disk)
left = 0
right = len(disk) - 1
while left <= right:
    # Move the left pointer until it points to a non-DELIMITER_STR element
    while left < len(disk) and disk[left] != DELIMITER_STR:
        left += 1

    # Move the right pointer until it points to a DELIMITER_STR element
    while right >= 0 and disk[right] == DELIMITER_STR:
        right -= 1

    # If left is less than or equal to right, swap the values
    if left <= right:
        disk[left], disk[right] = disk[right], disk[left]
        left += 1
        right -= 1

ans = 0
for i, char in enumerate(disk):
    if char != DELIMITER_STR:
        ans += i * ord(char)

print(ans)
