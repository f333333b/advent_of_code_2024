from collections import Counter

path = 'day1.txt'

with open(path) as file:
    data = file.read()
    formatted_data = data.replace('\n', ' ').split()
    left = sorted(formatted_data[::2])
    right = sorted(formatted_data[1::2])
    print(sum(
        [abs(int(right[i]) - int(left[i])) for i in range(len(left))]
    ))


# part 2
    c = Counter(right)
    total = 0
    for number in left:
        total += int(number) * c[number]
    print(total)