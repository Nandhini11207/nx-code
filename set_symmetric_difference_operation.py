_ = input()
english_set = set(map(int, input().split()))
_ = input()
french_set = set(map(int, input().split()))
exclusive_subscribers = english_set ^ french_set
print(len(exclusive_subscribers))