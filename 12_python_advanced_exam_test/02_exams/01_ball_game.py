from collections import deque

scored_goals = 0

strength = [int(x) for x in input().split()]
accuracy = deque(int(x) for x in input().split())

while strength and accuracy:
    kick = strength[-1]
    direct = accuracy[0]

    result = kick + direct

    if result == 100:
        scored_goals += 1
        strength.pop()
        accuracy.popleft()
    elif result < 100:
        if kick < direct:
            strength.pop()
        elif kick > direct:
            accuracy.popleft()
        elif kick == direct:
            accuracy.popleft()
            strength[-1] = result
    elif result > 100:
        strength[-1] -= 10
        accuracy.popleft()
        accuracy.append(direct)

if scored_goals == 3:
    print("Paul scored a hat-trick!")
elif scored_goals == 0:
    print("Paul failed to score a single goal.")
elif scored_goals > 3:
    print("Paul performed remarkably well!")
elif 0 < scored_goals < 3:
    print("Paul failed to make a hat-trick.")

if scored_goals > 0:
    print(f"Goals scored: {scored_goals}")

if strength:
    print(f"Strength values left: {', '.join(str(x) for x in strength)}")
if accuracy:
    print(f"Accuracy values left: {', '.join(str(x) for x in accuracy)}")