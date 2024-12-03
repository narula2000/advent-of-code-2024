stream = ""
with open("input.txt", "r") as file:
    for line in file:
        stream += line.strip()

ans = []
for idx, char in enumerate(stream):
    # Max valid length is mul(xxx,xxx) -> 12
    if char == "m":
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
