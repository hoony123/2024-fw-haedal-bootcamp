import sys
input = sys.stdin.readline

while True:
    a = input().rstrip()
    if not a:
        break
    s, t = a.split()
    f = 0
    k = 0
    
    for i in range(len(t)):
        if t[i] == s[k]:
            k+=1
            if k == len(s):
                f = 1
                break
    
    if f == 1:
        print('Yes')
    else:
        print('No')