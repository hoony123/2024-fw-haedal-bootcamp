a, b = int(input()), int(input())
s, e = 1, b

while s <= e:
    mid = (s + e) // 2
    
    t = 0
    for i in range(1, a+1):
        t += min(mid//i, a) 
    
    if t >= b: 
        answer = mid
        e = mid - 1
    else:
        s = mid + 1
print(answer)