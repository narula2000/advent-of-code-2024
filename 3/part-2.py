stream = ""
with open("input.txt", "r") as file:
    for line in file:
        stream += line.strip()

ans = []
flag = True
for idx, char in enumerate(stream):
    if char == "d":
        # do() -> 4
        do = stream[idx : idx + 4]
        # don't() -> 7
        dont = stream[idx : idx + 7]
        if do == "do()":
            flag = True
        if dont == "don't()":
            flag = False

    if flag and char == "m":
        # Max valid length is mul(xxx,xxx) -> 12
        to_check = stream[idx : idx + 12]
        if to_check[:4] == "mul(":
            for j, checking in enumerate(to_check[4:]):
                if checking == ")":
                    csv = to_check[4 : 4 + j]
                    values = csv.split(",")
                    print(to_check, csv)
                    if len(values) == 2:
                        left, right = values
                        try:
                            a, b = int(left), int(right)
                            ans.append(a * b)
                        except Exception:
                            break
                    break
print(ans)
print(sum(ans))
