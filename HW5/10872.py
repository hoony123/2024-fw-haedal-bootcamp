a = int(input())

def factorial(b):
    if b == 1 or b == 0:
        return 1
    return b * factorial(b - 1)

print(factorial(a))