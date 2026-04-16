n, k = map(int, input().split())
marks_matrix = []
for _ in range(k):
    marks_matrix.append(list(map(float, input().split())))
for student_marks in zip(*marks_matrix):
    average = sum(student_marks) / k
    print(f"{average:.1f}")
