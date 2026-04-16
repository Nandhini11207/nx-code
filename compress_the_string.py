from itertools import groupby
def compress_string():
    s = input().strip()
    results = []
    for key, group in groupby(s):
        count = len(list(group))
        results.append(f"({count}, {key})")
    print(" ".join(results))
if __name__ == "__main__":
    compress_string()