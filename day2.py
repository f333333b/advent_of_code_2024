path = 'day2.txt'
total_rows_p1 = 0
total_rows_p2 = 0

def sort_check_p1(row: list) -> bool:
    '''Функция проверки отсортированности списка (часть 1)'''
    if row == sorted(row) or row == sorted(row, reverse=True):
        return True
    return False

def diff_and_sort_check_p2(row: list) -> bool:
    '''Функция проверки отсортированности списка (часть 2)'''
    for i in range(len(row)):
        current_row = row[:i] + row[i + 1:]
        if sort_check_p1(current_row) and diff_check(current_row):
            return True
    return False

def diff_check(row: list) -> bool:
    '''Функция проверки разницы между соседними числами'''
    if all(1 <= abs(row[i] - row[i + 1]) <= 3 for i in range(len(row) - 1)):
        return True
    return False

with open(path) as file:
    data = [i.split() for i in map(str.strip, file.readlines())]

# part 1
for row in data:
    row = list(map(int, row))
    total_rows_p1 += int(sort_check_p1(row) and diff_check(row))

# part 2
for row in data:
    row = list(map(int, row))
    if diff_and_sort_check_p2(row):
        total_rows_p2 += 1

print(f'Total rows (part 1) = {total_rows_p1}')
print(f'Total rows (part 2) = {total_rows_p2}')
