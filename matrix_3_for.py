A=[[13, 10, 4],
   [22, 4, 99]]

B=[[9, 3],
   [5, 5],
   [3, 9]]

n=len(A)
m=len(B[0])
p=len(B)
C=[]
for i in range(n):
    row=[]
    for j in range(m):
        row.append(0)
    C.append(row)
for i in range(n):
    for j in range(m):
        for k in range(p):
            C[i][j]+=A[i][k] * B[k][j]

print(C)