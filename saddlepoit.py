a=[[0,1,1,1,7],
   [2,3,4,5,6],
   [3,6,5,8,7],
   [2,5,8,6,9],
   [2,3,5,4,8]]

b = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


for i in range(5):
    for j in range(5):
        if(max(a[i])==min(b[j])):
            print(a[i][j])
            print(i+1,j+1)
