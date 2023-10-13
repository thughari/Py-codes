def solve(N,A,D,V):
    res=[]
    f=0
    if(D=='bank_account_number'):
        f=0
    elif(D=='account_holder_first_name'):
        f=1
    elif(D=='account_holder_last_name'):
        f=2
    elif(D=='registered_mobile_number'):
        f=3
    elif(D=='branch_code'):
        f=4
    for i in range(N):
        if(A[i][f]==V):
            res.append(A[i])
    res.sort(key=lambda x:x[0])
    return res

    




'''N=int(input())
A=[input().split() for i in range(N)]
D=input()
V=input()'''

N=3
A=[['11221909312','rohan','garg','7384713384','1022'],
    ['11221909566','shivam','kumar','9128494856','1022'],
    ['11201339211','shivam','sharma','7984728384','1987']]
D='account_holder_first_name'
V='shivam'

out_=solve(N,A,D,V)
