n = int(input())

elements = set()

for _ in range(n):
    chemical_compounds = input().split()
    for el in chemical_compounds:
        elements.add(el)

for chemical_element in elements:
    print(chemical_element)
