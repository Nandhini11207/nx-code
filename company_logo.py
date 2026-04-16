from collections import Counter
if __name__ == '__main__':
    s = input().strip()
    s_sorted=sorted(s)
    counts=Counter(s_sorted)
    most_common_three=counts.most_common(3)
    for char,count in most_common_three:
        print(f"{char} {count}")