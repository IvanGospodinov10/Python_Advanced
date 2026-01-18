rows, cols = map(int, input().split(", "))

matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

max_sum = float("-inf")
sub_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        first_element = matrix[row][col]
        second_element = matrix[row][col + 1]
        third_element = matrix[row + 1][col]
        forth_element = matrix[row + 1][col + 1]

        current_sum = first_element + second_element + third_element + forth_element
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[first_element, second_element], [third_element, forth_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)