N,W=map(int,input().split())
 
#S = [[0 for j in range(3)] for i in range(2)]　2行3列の場合
S = [[0 for j in range(2)] for i in range(N*2)]
 
for i in range(N):
    A,B,l=map(int,input().split())
    S[i][0]=A
    S[i][1]=l
    S[i+N][0]=B+1
    S[i+N][1]=-l
 
T=sorted(S,key=lambda x:x[0])
 
#print(T)
ans=0
tmp=0
 
for i in range((2*N)-1):
    tmp+=T[i][1]
    #print(tmp)
    if tmp<=W:
        #print("1")
        ans+= tmp*(T[i+1][0]-T[i][0])
    else:
        ans+= W*(T[i+1][0]-T[i][0])
        #print("e")
    
print(ans)
