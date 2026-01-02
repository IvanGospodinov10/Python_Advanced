from collections import deque

class Robot:
    def __init__(self, name, process_time):
        self.name = name
        self.process_time = process_time
        self.busy_until = 0

    def is_free(self, current_time):
        return current_time >= self.busy_until

    def assign(self, product, current_time):
        self.busy_until = current_time + self.process_time
        return f"{self.name} - {product} [{format_time(current_time)}]"

def format_time(seconds):
    seconds %= 24 * 3600
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

# --- Input parsing ---

robots_input = input().split(";")
robots = []
for line in robots_input:
    name, process_time = line.split("-")
    robots.append(Robot(name,int(process_time)))

start_time = list(map(int, input().split(":")))
print(start_time)
current_time = start_time[0] * 3600 + start_time[1] * 60 + start_time[2]
print(current_time)

products = deque()

while True:
    line = input()
    if line == "End":
        break
    products.append(line)

# --- Simulation ---

while products:
    current_time += 1
    product = products.popleft()

    assigned = False

    for robot in robots:
        if robot.is_free(current_time):
            print(robot.assign(product, current_time))
            assigned = True
            break

    if not assigned:
        products.append(product)