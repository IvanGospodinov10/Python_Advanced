n = int(input())
my_stack = []

function = {
    "1": lambda x: my_stack.append(x),
    "2": lambda: my_stack.pop() if my_stack else None,
    "3": lambda: max(my_stack) if my_stack else None,
    "4": lambda: min(my_stack)if my_stack else None,
}

for _ in range(n):
    query = input().split()
    function[query[0]](*query[1:])
print(" ".join([str(x) for x in reversed(my_stack)]))