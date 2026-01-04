students = int(input())

student_record = {}

for _ in range(students):
    data = input().split()
    name = data[0]
    grade = float(data[1])

    if name not in student_record:
        student_record[name] = []
    student_record[name].append(grade)

for name, grades in student_record.items():
    average_grades = sum(grades) / len(grades)
    grades_as_str = [f"{el:.2f}" for el in grades]
    print(f"{name} -> {' '.join(grades_as_str)} (avg: {average_grades:.2f})")