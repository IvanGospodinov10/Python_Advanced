n = int(input())

user_names = set()

for _ in range(n):
    username = input()
    user_names.add(username)

for user in user_names:
    print(user)