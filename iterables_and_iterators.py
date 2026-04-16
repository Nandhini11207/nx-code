from itertools import combinations
def solve_probability():
    n = int(input())
    letters = input().split()
    k = int(input())
    all_combos = list(combinations(range(n), k))
    indices_with_a = [i for i, char in enumerate(letters) if char == 'a']
    count = 0
    for combo in all_combos:
        if any(idx in indices_with_a for idx in combo):
            count += 1
    print(round(count / len(all_combos), 4))
if __name__ == "__main__":
    solve_probability()
