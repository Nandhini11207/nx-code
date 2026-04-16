from itertools import combinations
def solve():
    data = input().split()
    s = sorted(data[0]) 
    k = int(data[1])
    for i in range(1, k + 1):
        combos = combinations(s, i)
        for c in combos:
            print("".join(c))
if __name__ == "__main__":
    solve()
