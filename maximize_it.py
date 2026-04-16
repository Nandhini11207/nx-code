from itertools import product
def solve():
    k, m = map(int, input().split())
    all_lists = []
    for _ in range(k):
        row = list(map(int, input().split()))[1:]
        all_lists.append(row)
    combinations = product(*all_lists)
    max_val = 0
    for combo in combinations:
        current_val = sum(x**2 for x in combo) % m
        if current_val > max_val:
            max_val = current_val
    print(max_val)
if __name__ == "__main__":
    solve()