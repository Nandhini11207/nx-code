from itertools import combinations_with_replacement
def solve():
    data = input().split()
    s = sorted(data[0])
    k = int(data[1])
    combos = combinations_with_replacement(s, k)
    for c in combos:
        print("".join(c))
if __name__ == "__main__":
    solve()
