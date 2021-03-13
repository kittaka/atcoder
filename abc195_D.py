import copy
N,M,Q=map(int,input().split())
S = [[0 for j in range(2)] for i in range(N+1)]
 
#DP= [[0 for j in range(100010)] for i in range(110)]
def chmax(a,b):
    if a>b:
        return a
    else:
        return b
 
 
for i in range(N):
    w,v=map(int,input().split())
    S[i][0]=w
    S[i][1]=v
X=list(map(int,input().split()))
SS=sorted(S,key=lambda x: x[1], reverse=True)
done=[-1]*len(SS)
 
for i in range(Q):
    ans=0
    done=[-1]*len(SS)
    tmp=copy.deepcopy(X)
    tmpS=copy.deepcopy(SS)
    l,r=map(int,input().split())
    for j in reversed(range(l-1,r)):
        tmp.pop(j)
    
    tmp.sort()
    #print(tmp)
    for j in range(len(tmp)):
        for k in range(len(SS)):
            if tmpS[k][0]<=tmp[j]:
                if done[k]==-1:
                    ans+=tmpS[k][1]
                    done[k]=1
                    break
                
    print(ans)
