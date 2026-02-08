def plant_garden(space, *args, **kwargs):
    request = dict(sorted(kwargs.items()))
    planted_flowers = {}
    allowed_flowers = {plant: area for plant, area in args}

    fully_planted = True

    for flower, quantity in request.items():
        if flower not in allowed_flowers:
            continue

        area_per_piece = allowed_flowers[flower]
        required_space = quantity * area_per_piece

        # Ако няма място за всички
        if space < required_space:
            allowed_plant_flower = int(space // area_per_piece)

            if allowed_plant_flower > 0:
                planted_flowers[flower] = allowed_plant_flower
                space -= allowed_plant_flower * area_per_piece
                fully_planted = False
            else:
                fully_planted = False

            continue

        # Има място за всички
        planted_flowers[flower] = quantity
        space -= required_space

    # Проверка за успех
    all_allowed_requests = {p: q for p, q in request.items() if p in allowed_flowers}

    all_full = True
    for plant, requested_qty in all_allowed_requests.items():
        if plant not in planted_flowers or planted_flowers[plant] != requested_qty:
            all_full = False
            break

    result = []

    if fully_planted and all_full:
        result.append(f"All plants were planted! Available garden space: {space:.1f} sq meters.")
    else:
        result.append("Not enough space to plant all requested plants!")

    result.append("Planted plants:")
    for plant in sorted(planted_flowers):
        result.append(f"{plant}: {planted_flowers[plant]}")

    return "\n".join(result)


print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))
