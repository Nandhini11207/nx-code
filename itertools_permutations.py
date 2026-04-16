from itertools import permutations
if __name__ == '__main__':
    s, k = input().split()
    k = int(k)
    s_sorted = sorted(s)
    perms = list(permutations(s_sorted, k))
    for p in perms:
        print("".join(p))