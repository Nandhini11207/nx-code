from collections import deque
def solve_stacking():
    try:
        t = int(input())
    except EOFError:
        return
    for _ in range(t):
        n = int(input())
        cubes = deque(map(int, input().split()))
        top_cube = float('inf')
        possible = True
        while cubes:
            if cubes[0] >= cubes[-1]:
                current = cubes.popleft()
            else:
                current = cubes.pop()
            if current > top_cube:
                possible = False
                break
            top_cube = current
        print("Yes" if possible else "No")
if __name__ == "__main__":
    solve_stacking()
