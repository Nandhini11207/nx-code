if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    unique_scores = sorted(set(score for name, score in students))
    second_lowest_grade = unique_scores[1]
    runner_up_names = sorted([name for name, score in students if score == second_lowest_grade])
    for name in runner_up_names:
        print(name)
