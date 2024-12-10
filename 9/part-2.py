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


def move_chunks(disk, delimiter=DELIMITER_STR):
    # Convert the input string into a list for mutable manipulation
    disk_list = list(disk)
    seen = set()

    # Step 1: Process chunks from right to left
    position = len(disk_list) - 1
    print("Length:", position)
    iter = 0
    while position >= 0:
        if iter % 1000 == 0:
            print(iter)
        iter += 1
        # Identify the current chunk (sequence of identical characters)
        current_chunk = []
        current_char = disk_list[position]
        while (
            position >= 0
            and current_char == disk_list[position]
            and current_char != delimiter
        ):
            current_chunk.insert(0, disk_list[position])
            position -= 1

        # If a chunk was identified
        if current_chunk and "".join(current_chunk) not in seen:
            chunk_length = len(current_chunk)

            # Find the first available position on the left with enough delimiters
            for i in range(len(disk_list) - chunk_length + 1):
                if i > position:
                    break
                if all(disk_list[j] == delimiter for j in range(i, i + chunk_length)):
                    # Move the chunk to the leftmost available position
                    disk_list[i : i + chunk_length] = current_chunk

                    # Replace the original chunk position with delimiters
                    for k in range(chunk_length):
                        disk_list[position + 1 + k] = delimiter
                    break
        seen.add("".join(current_chunk))

        # Skip over the delimiters
        while position >= 0 and disk_list[position] == delimiter:
            position -= 1

    # Step 2: Return the final transformed string
    return "".join(disk_list)


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
disk = move_chunks(disk)

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
disk = move_chunks(disk)

ans = 0
for i, char in enumerate(disk):
    if char != DELIMITER_STR:
        ans += i * ord(char)

print(ans)
