import re
from operator import mul

path = 'day03.txt'
pattern = r'mul\(\d{1,3},\d{1,3}\)'

with open(path) as file:
    data = file.read()
    matches = re.findall(pattern, data)
    result = sum(eval(pair) for pair in matches)

print(f'Result (part 1): {result}')

# part 2
def mul_adder():
    pass

checker = True
chunk = data
matches_p2 = []

# solution 1
while chunk:
    try:
        separator = chunk.index("don't()")
        processed_chunk = chunk[:separator]
        matches_p2 += re.findall(pattern, processed_chunk)
        chunk = chunk[separator:]
        chunk = chunk[chunk.index('do()'):]
    except:
        matches_p2 += re.findall(pattern, chunk)
        chunk = False

result_p2 = sum(eval(pair) for pair in matches_p2)

print(f'Result (part 2) (solution # 1): {result_p2}')

# solution 2
# отрезок до первого don't()
first_part = re.findall(pattern, data[:data.index("don't()")])

# основная часть
pattern_p2 = r"do\(\).*?don't\(\)"
second_part_do_dont = re.findall(pattern_p2, data)
second_part_matrix = [re.findall(pattern, i) for i in second_part_do_dont]
second_part = [x for l in second_part_matrix for x in l]

# последний отрезок - от последнего do() до конца, если нет don't
if data.rindex('do()') > data.rindex("don't()"):
    third_part = re.findall(pattern, data[data.rindex('do()'):])

total_matches = first_part + second_part + third_part if third_part else 0
result_p2 = sum(eval(pair) for pair in matches_p2)
print(f'Result (part 2) (solution # 2): {result_p2}')