N,M=map(int,input().split())
arr = [[0 for i in range(2)] for j in range(N)]
goukei=0
count=0
for i in range(N):
    arr[i][0],arr[i][1]=map(int,input().split())
    
    
k=0    
arr.sort()
while M-count>0:
    goukei+=arr[k][0]
    arr[k][1]-=1
    
    if arr[k][1]==0:
        k+=1
    
    count+=1
 
print(goukei)