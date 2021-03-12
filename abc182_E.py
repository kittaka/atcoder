from collections import deque


H,W,N,M=map(int,input().split())
#S=[[0] * 3 for _ in range(2)] 2行3列の場合
S=[[0] * W for _ in range(H)]
L=[[0] * W for _ in range(H)]
L2=[[0] * W for _ in range(H)]

for i in range(N):
    A,B=map(int,input().split())
    S[A-1][B-1]=1
    
for i in range(M):
    A,B=map(int,input().split())
    S[A-1][B-1]=-1
#print(S)





for i in range(H):
    for j in range(W):
        if S[i][j]==1:
            t=i
            tt=i
            
            if L[i][j]!=1:
                while t<H:
                    if S[t][j]!=-1:
                        L[t][j]=1
                        t+=1
                    else:
                        break
                while tt>=0:
                    if S[tt][j]!=-1:
                        L[tt][j]=1
                        tt-=1
                    else:
                        break
for i in range(H):
    for j in range(W):
        if S[i][j]==1:

            m=j
            mm=j

            if L2[i][j]!=1:
                while m<W:
                    if S[i][m]!=-1:
                        L2[i][m]=1
                        m+=1
                    else:
                        break
                while mm>=0:
                    if S[i][mm]!=-1:
                        L2[i][mm]=1
                        mm-=1
                    else:
                        break
cnt=0
for i in range(H):
    for j in range(W):
        if L[i][j]==1 or L2[i][j]==1:
            cnt+=1
print(cnt)
#print(L)
#print(L2)
