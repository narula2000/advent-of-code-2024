left_lst, right_lst = [], []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        left, right = line.split()
        left_lst.append(int(left))
        right_lst.append(int(right))


left_lst.sort()
right_lst.sort()

answer = sum([abs(left-right) for left, right in zip(left_lst, right_lst)])
print(answer)

