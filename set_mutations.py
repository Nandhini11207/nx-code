_ = input()
a = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    operation = input().split()[0]
    other_set = set(map(int, input().split()))
    getattr(a, operation)(other_set)
print(sum(a))
