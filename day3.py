import re
from operator import mul

path = 'day3.txt'
pattern = r'mul\(\d{1,3},\d{1,3}\)'

with open(path) as file:
    data = file.read()
    matches = re.findall(pattern, data)
    result = sum(eval(pair) for pair in matches)

print(result)

# part 2