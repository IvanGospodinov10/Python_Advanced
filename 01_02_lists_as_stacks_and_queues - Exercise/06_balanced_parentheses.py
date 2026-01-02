expression = input()

parentheses = {"(": ")", "[": "]", "{": "}"}
stack = []

for char in expression:
    if char in parentheses:
        stack.append(char)
    elif char in parentheses.values():
        if not stack:
            print("NO")
            break
        last_opening_parenthesis = stack.pop()
        if parentheses[last_opening_parenthesis] != char:
            print("NO")
            break
else:
    if stack:
        print("NO")
    else:
        print("YES")
