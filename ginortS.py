def custom_sort_key(char):
    if char.islower():
        return (0, char)
    elif char.isupper():
        return (1, char)
    elif char.isdigit() and int(char) % 2 != 0:
        return (2, char)
    else:
        return (3, char)
s = input().strip()
sorted_chars = sorted(s, key=custom_sort_key)
print("".join(sorted_chars))
