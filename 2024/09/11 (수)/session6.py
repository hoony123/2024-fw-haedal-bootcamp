'''def hanoi(n, source, target, auxiliary):
    if n == 1 :
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, auxiliary, target, source)

hanoi(3, 'A', 'C', 'B')'''

'''def max_of(a):
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    print(maximum)
    return maximum
    


b=[1,4,5,6,7,8,9,10]

max_of(b)'''


def max_of(a):
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    print(maximum)
    return maximum


print('배열의 최댓값을 구합니다.')
a=int(input('원소 수를 입력하세요 : '))
i = []
k=0
for k in a :
    b=int(input('x[k]값을 입력하세요 : '))
    i.append(b)

max_of(i)








