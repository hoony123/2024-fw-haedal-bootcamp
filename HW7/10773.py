a = int(input())

s = []

for _ in range(a) :
    b = int(input())
    if b == 0 :
        s.pop()
    else :
        s.append(b)

print(sum(s))