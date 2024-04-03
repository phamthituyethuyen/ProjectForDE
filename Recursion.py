#the limit recursion value
from sys import getrecursionlimit
a =getrecursionlimit()
print(a)

#đếm ngược về sô 0
def countdown(n):
    print(n)
    if n==0:
        return 
    else:
        countdown(n -1)
countdown(5)

#TÍnh giai thừa
def giaithua(n):
    return 1 if n<=1 else n * giaithua(n - 1)
print(giaithua(5))