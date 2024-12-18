with open('input.txt') as file:
    text = file.readlines()
matrix = [[0] * 101 for _ in range(103)]
robots = []
sum_q1, sum_q2, sum_q3, sum_q4 = 0, 0, 0, 0

def move(robot_num, robot, velocity):
    row, col = robot
    v1, v2 = velocity
    matrix[row][col] -= 1
    new_row, new_col = (row + v1) % 103, (col + v2) % 101
    matrix[new_row][new_col] += 1
    robots[robot_num][robot_num][0] = [new_row, new_col]

for sub_t in range(len(text)):
    col, row = [int(i) for i in text[sub_t].strip().split()[0][2:].split(',')]
    v2, v1 = [int(i) for i in text[sub_t].strip().split()[1][2:].split(',')]
    robots.append({sub_t: [[row, col], [v1, v2]]})
    matrix[row][col] += 1

for second in range(100):
    for robot in robots:
        for key, value in robot.items():
            move(key, value[0], value[1])

for i in range(103):
    for j in range(101):
        if i < 51 and j < 50:  # Q1
            sum_q1 += matrix[i][j]
        elif i < 51 and j > 50:  # Q2
            sum_q2 += matrix[i][j]
        elif i > 51 and j < 50:  # Q3
            sum_q3 += matrix[i][j]
        elif i > 51 and j > 50:  # Q4
            sum_q4 += matrix[i][j]

print(sum_q1 * sum_q2 * sum_q3 * sum_q4)