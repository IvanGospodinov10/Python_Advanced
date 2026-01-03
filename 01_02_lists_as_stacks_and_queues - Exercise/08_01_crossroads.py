from collections import deque

class Car:
    def __init__(self, car_name):
        self.car_name = car_name
        self.length = len(car_name)

    def hit_at(self, index):
        return self.car_name[index]

class Crossroads:
    def __init__(self, green_light_, free_window_):
        self.green_light_ = green_light_
        self.free_window_ = free_window_
        self.queue = deque()
        self.passed = 0

    def add_car(self, car):
        self.queue.append(car)

    def process_green_light(self):
        current_green_light = self.green_light_

        while self.queue and current_green_light > 0:
            car = self.queue.popleft()
            car_length = car.length

            if car_length <= current_green_light:
                current_green_light -= car_length
                self.passed += 1
            else:
                remaining = car_length - current_green_light

                if remaining <= self.free_window_:
                    self.passed += 1
                else:

                    hit_index = current_green_light + self.free_window_
                    print("A crash happened!")
                    print(f"{car.car_name} was hit at {car.hit_at(hit_index)}.")
                    raise SystemExit

                current_green_light = 0

    def finish(self):
        print("Everyone is safe.")
        print(f"{self.passed} total cars passed the crossroads.")


green_light = int(input())
free_window = int(input())

crossroads = Crossroads(green_light, free_window)

while True:
    command = input()

    if command == "END":
        break

    if command == "green":
        crossroads.process_green_light()
    else:
        crossroads.add_car(Car(command))

crossroads.finish()

