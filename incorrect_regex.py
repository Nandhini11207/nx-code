import re
import sys
def check_valid_regex():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    t = int(data[0])
    for i in range(1, t + 1):
        regex_string = data[i]
        try:
            re.compile(regex_string)
            print("True")
        except re.error:
            print("False")
if __name__ == "__main__":
    check_valid_regex()
