from collections import namedtuple
n = int(input())
Student = namedtuple('Student', input().split())
marks = [int(Student(*input().split()).MARKS) for _ in range(n)]
print(f"{sum(marks) / n:.2f}")
