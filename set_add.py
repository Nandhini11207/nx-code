def count_distinct_stamps():
    try:
        n = int(input())
    except EOFError:
        return
    country_set = set()
    for _ in range(n):
        country = input().strip()
        country_set.add(country)
    print(len(country_set))
if __name__ == "__main__":
    count_distinct_stamps()
