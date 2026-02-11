def list_roman_emperors(*emperors, **emperors_rules):
    successful_emperors = {}
    unsuccessful_emperors = {}

    for emperor in emperors:
        emperor_name = emperor[0]
        emperor_success = emperor[1]

        if emperor_success:
            successful_emperors[emperor_name] = ""
        else:
            unsuccessful_emperors[emperor_name] = ""
    for emperor_rule, ages in emperors_rules.items():
        if emperor_rule in successful_emperors:
            successful_emperors[emperor_rule] = ages
        else:
            unsuccessful_emperors[emperor_rule] = ages

    successful_emperors_sort = sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0]))
    unsuccessful_emperors_sort = sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0]))

    result = []

    number_of_emperors = len(successful_emperors_sort) + len(unsuccessful_emperors_sort)
    result.append(f"Total number of emperors: {number_of_emperors}")

    if successful_emperors_sort:
        result.append("Successful emperors:")
        for emperor, ages in successful_emperors_sort:
            result.append(f"****{emperor}: {ages}")

    if unsuccessful_emperors_sort:
        result.append("Unsuccessful emperors:")
        for emperor, ages in unsuccessful_emperors_sort:
            result.append(f"****{emperor}: {ages}")

    return "\n".join(result)


print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14, ))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False),
                          ("Pertinax", False), ("Vespasian", True),
                          Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19, ))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True),
                          Augustus=40, Trajan=19, Claudius=13, ))
