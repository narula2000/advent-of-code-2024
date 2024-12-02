from collections import Counter

left_lst, right_lst = [], []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        left, right = line.split()
        left_lst.append(int(left))
        right_lst.append(int(right))

count = Counter(right_lst)

answer = sum([left*count.get(left, 0) for left in left_lst])
print(answer)

