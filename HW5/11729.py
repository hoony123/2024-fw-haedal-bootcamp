def h(num, s, e):
    if num == 1:
        print(s, e)
        return
    else:
        h(num-1, s, 6-s-e)
        print(s, e)
        h(num-1, 6-s-e, e)

a = int(input())

print(2**a -1)
h(a, 1, 3)