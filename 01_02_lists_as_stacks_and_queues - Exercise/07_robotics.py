from collections import deque

def format_time(seconds):
    seconds %= 24 * 3600
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

robots_input = input().split(";")
robots = []
for robot in robots_input:
    name, time = robot.split("-")
    robots.append([name, int(time), 0])
# print(robots)

start_time = list(map(int, input().split(":")))
current_time = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]

products = deque()
while True:
    line = input()
    if line == "End":
        break
    products.append(line)

while products:
    current_time += 1
    product = products.popleft()

    assigment = False
    for robot in robots:
        test = robot
        name, process_time, busy_until = robot
        if current_time >= busy_until:
            robot[2] = current_time + process_time
            print(f"{name} - {product} [{format_time(current_time)}]")
            assigment = True
            break
    if not assigment:
        products.append(product)

