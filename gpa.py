
#h=[7.46,7.25,6.77,6.36,7.48,7.19,6.45]

#s=[7.70,7.46,7.32,6.32,7.05,7.33,6.72]

n=int(input("no of semesters "))
s=[]
ac=[24,24,22,22,21,21,22,24]
c=ac[:]
cg=0
sac=0
for i in range(n):
    s.append(float(input(f"enter {i+1} semester GPA: ")))
    c[i]=c[i]-(int(input(f"no of backlogs in {i+1} semester: "))*3)
    cg+=s[i]*c[i]
    sac+=ac[i]

res=cg/sac
res=res-0.75
print(res*10)