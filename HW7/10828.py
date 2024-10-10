import sys
input=sys.stdin.readline

n=int(input())
s=[]

def push(p):
    s.append(p)

def pop():
    if len(s)!=0:
        print(s.pop())
    else:
        print(-1)

def size():
    print(len(s))

def empty():
    if len(s)==0:
        print(1)
    else:
        print(0)

def top():
    if len(s)!=0:
        print(s[-1])
    else:
        print(-1)
    
for i in range(n):
    c=input().split()
    if c[0]=='push':
        push(c[1])
    elif c[0]=='pop':
        pop()
    elif c[0]=='size':
        size()
    elif c[0]=='empty':
        empty()
    elif c[0]=='top':
        top()