def solve_symmetric_difference():
    _ = input() # Skip size M
    a = set(map(int, input().split()))
    _ = input() # Skip size N
    b = set(map(int, input().split()))
    diff = a ^ b
    for val in sorted(diff):
        print(val)
if __name__ == "__main__":
    solve_symmetric_difference()
