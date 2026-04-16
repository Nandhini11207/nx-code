def solve_union():
    _ = input() 
    english_set = set(map(int, input().split()))
    _ = input() 
    french_set = set(map(int, input().split()))
    all_subscribers = english_set | french_set
    print(len(all_subscribers))
if __name__ == "__main__":
    solve_union()