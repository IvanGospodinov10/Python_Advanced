n = int(input())

reservations = set()

for _ in range(n):
    reservations.add(input())

reservation = input()

while reservation != "END":
    if reservation in reservations:
        reservations.remove(reservation)
    reservation = input()

print(len(reservations))

sorted_reservations = sorted(reservations)

for number in sorted_reservations:
    print(number)
