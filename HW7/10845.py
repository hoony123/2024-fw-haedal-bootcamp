import sys

def push(x):
    queue.append(x)

def pop():
    if(not queue):
        return -1
    else:
        return queue.pop(0)

def size():
    return len(queue)

def empty():
    return 0 if queue else 1

def front():
    return queue[0] if queue else -1

def back():
    return queue[-1] if queue else -1

N = int(sys.stdin.readline().rstrip())
queue = []

for _ in range(N):
    i = sys.stdin.readline().rstrip().split()

    a = i[0]

    if a == "push":
        push(i[1])
    elif a == "pop":
        print(pop())
    elif a == "size":
        print(size())
    elif a == "empty":
        print(empty())
    elif a == "front":
        print(front())
    elif a == "back":
        print(back())