from collections import deque
def solve_deque():
    try:
        n = int(input())
    except EOFError:
        return
    d = deque()
    for _ in range(n):
        line = input().split()
        command = line[0]
        if len(line) > 1:
            val = line[1]
            getattr(d, command)(val)
        else:
            getattr(d, command)()
    print(*(d))
if __name__ == "__main__":
    solve_deque()
