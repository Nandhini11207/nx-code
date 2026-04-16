def solve(s):
    for word in s.split():
        s = s.replace(word, word.capitalize())
    return s
def solve_robust(s):
    words = s.split(' ')
    return ' '.join(word.capitalize() for word in words)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()