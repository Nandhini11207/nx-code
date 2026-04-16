def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    width = (size * 4) - 3
    lines = []
    for i in range(size):
        s = "-".join(alpha[size-1:size-i-1:-1] + alpha[size-i-1:size])
        lines.append(s.center(width, "-"))
    print('\n'.join(lines + lines[:-1][::-1]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)