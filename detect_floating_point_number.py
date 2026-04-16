import re
for _ in range(int(input())):
    s = input()
    try:
        is_float = bool(float(s)) 
        print(bool(re.match(r'^[+-]?[0-9]*\.[0-9]+$', s)))
    except ValueError:
        print(False)
