from collections import OrderedDict
def main():
    n = int(input())
    item_dict = OrderedDict()
    for _ in range(n):
        data = input().split()
        price = int(data[-1])
        item_name = " ".join(data[:-1])
        if item_name in item_dict:
            item_dict[item_name] += price
        else:
            item_dict[item_name] = price
    for item, net_price in item_dict.items():
        print(f"{item} {net_price}")
if __name__ == "__main__":
    main()