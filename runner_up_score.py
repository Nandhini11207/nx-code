if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores=sorted(set(arr))
    runner=scores[-2]
    print(runner)
