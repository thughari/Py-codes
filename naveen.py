
def findMessages (N, A):
    A=' '.join(A)
    t='abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        A = A.replace(t[i], t[-i-1])
    return len(set(A.split()))

N = int(input())
A = list(input().split())

out_ = findMessages(N, A)
print (out_)