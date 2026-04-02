if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        command = input().split()
        cmd_type = command[0]
        if cmd_type == "insert":
            index = int(command[1])
            element = int(command[2])
            my_list.insert(index, element)
        elif cmd_type == "print":
            print(my_list)
        elif cmd_type == "remove":
            element = int(command[1])
            my_list.remove(element)
        elif cmd_type == "append":
            element = int(command[1])
            my_list.append(element)
        elif cmd_type == "sort":
            my_list.sort()
        elif cmd_type == "pop":
            my_list.pop()
        elif cmd_type == "reverse":
            my_list.reverse()
