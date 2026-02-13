def accommodate(*guests, **rooms):
    guests = list(guests)
    unaccommodated_guest = 0

    rooms = dict(sorted(rooms.items(), key=lambda x: (x[1], x[0])))

    accommodated_rooms = {}

    while guests:
        guest_group = guests.pop(0)
        accommodated = False

        for room, capacity in list(rooms.items()):
            if guest_group <= capacity:
                accommodated_rooms[room] = guest_group
                del rooms[room]
                accommodated = True
                break

        if not accommodated:
            unaccommodated_guest += guest_group

    if accommodated_rooms:
        result = f"A total of {len(accommodated_rooms)} accommodations were completed!\n"
        accommodated_rooms = dict(sorted(accommodated_rooms.items(), key=lambda x: x[0]))

        for room, guests_accommodates in accommodated_rooms.items():
            room_number = room.split("_")[1]
            result += f"<Room {room_number} accommodates {guests_accommodates} guests>\n"

        if unaccommodated_guest:
            result += f"Guests with no accommodation: {unaccommodated_guest}\n"

        if rooms:
            result += f"Empty rooms: {len(rooms)}"

        return result.strip()

    else:
        result = "No accommodations were completed!\n"

        if unaccommodated_guest:
            result += f"Guests with no accommodation: {unaccommodated_guest}\n"

        if rooms:
            result += f"Empty rooms: {len(rooms)}"

        return result.strip()


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))
