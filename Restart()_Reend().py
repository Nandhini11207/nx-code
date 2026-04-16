import re
S = input()
k = input()
pattern = re.compile(r'(?=(' + k + '))')
matches = list(pattern.finditer(S))
if matches:
    for m in matches:
        print(f"({m.start()}, {m.start() + len(k) - 1})")
else:
    print("(-1, -1)")
