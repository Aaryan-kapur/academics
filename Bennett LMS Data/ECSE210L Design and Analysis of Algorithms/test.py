from random import seed
from random import choice
A=[1, -1, -1, 1, 1, 1 -1, 1]
T=[]
for i in range(len(A)):
    temp=[]
    for j in range(len(A)):
            temp.append(0)
    T.append(temp)

sequence=[-1, 1]
for i in range(len(A)):
    for j in range(len(A)):
        if i==j: 
            T[i][j]=0
        elif A[i]==1 and A[j]==1:
            T[i][j]=1
        elif A[i]==1 and A[j]==-1:
            T[i][j]=-1
        else:
            T[i][j]=choice(sequence)
print(T)    