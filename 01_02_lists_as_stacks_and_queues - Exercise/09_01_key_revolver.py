from collections import deque


class BulletStack:
    def __init__(self, bullets):
        self.bullets = bullets

    def has_bullets(self):
        return len(self.bullets) > 0

    def pop(self):
        return self.bullets.pop()

    def count(self):
        return len(self.bullets)


class LockQueue:
    def __init__(self, locks):
        self.locks = deque(locks)

    def has_locks(self):
        return len(self.locks) > 0

    def peek(self):
        return self.locks[0]

    def remove(self):
        return self.locks.popleft()

    def count(self):
        return len(self.locks)


class Gun:
    def __init__(self, barrel_size):
        self.barrel_size = barrel_size
        self.current_barrel = barrel_size

    def shoot(self):
        self.current_barrel -= 1

    def need_reload(self):
        return self.current_barrel == 0

    def reload(self):
        self.current_barrel = self.barrel_size


class Mission:
    def __init__(self, price_per_bullet, barrel_size, bullets, locks, money):
        self.price_per_bullet = price_per_bullet
        self.money = money

        self.bullets = BulletStack(bullets)
        self.locks = LockQueue(locks)
        self.gun = Gun(barrel_size)

        self.bullets_fire = 0

    def start_mission(self):
        while self.bullets.has_bullets() and self.locks.has_locks():
            bullet = self.bullets.pop()
            lock = self.locks.peek()

            self.bullets_fire += 1
            self.gun.shoot()

            if bullet <= lock:
                print("Bang!")
                self.locks.remove()
            else:
                print("Ping!")

            if self.gun.need_reload() and self.bullets.has_bullets():
                print("Reload!")
                self.gun.reload()
        self._print_result()

    def _print_result(self):
        if not self.locks.has_locks():
            bullets_left = self.bullets.count()
            money_left = self.money - self.bullets_fire * self.price_per_bullet
            print(f"{bullets_left} bullets left. Earned ${money_left}")
        else:
            print(f"Couldn't get through. Locks left: {self.locks.count()}")


# ----------------
# Input handling
# ----------------

price_per_bullet = int(input())
barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = list(map(int, input().split()))
money = int(input())

mission = Mission(price_per_bullet, barrel_size, bullets, locks, money)
mission.start_mission()
