cube = lambda x: x**3
def fibonacci(n):
    res = [0, 1]
    if n < 2:
        return res[:n]
    for i in range(2, n):
        res.append(res[-1] + res[-2])
    return res
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))