n = int(input())
s = set(map(int, input().split()))
num_commands = int(input())
for _ in range(num_commands):
    command = input().split()
    method = command[0]
    if method == "pop":
        s.pop()
    elif method == "remove":
        s.remove(int(command[1]))
    elif method == "discard":
        s.discard(int(command[1]))
print(sum(s))
