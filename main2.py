# coding: utf-8
# Your code here!
import statistics

N=int(input())
S=list(map(int,input().split()))

S1=[]
for i in range(N):
    S1.append(S[i]-i)
S1.sort()
chuouchi=statistics.median_high(S1)
chuouchi2=statistics.median_low(S1)
chuouchi3=statistics.median(S1)
ans=10**20
ansj=0
A=chuouchi-4
B=chuouchi+4
C=chuouchi2-4
D=chuouchi2+4
E=int(chuouchi3)-4
F=int(chuouchi3)+4
for i in range(A,B):
    goukei=0
    for j in range(N):
        goukei+=abs(S[j]-(i+j+1))
        
    if ans>goukei:
        ans=goukei
        
for i in range(C,D):
    goukei=0
    for j in range(N):
        goukei+=abs(S[j]-(i+j+1))
        
    if ans>goukei:
        ans=goukei

for i in range(E,F):
    goukei=0
    for j in range(N):
        goukei+=abs(S[j]-(i+j+1))
        
    if ans>goukei:
        ans=goukei        
        
print(ans)


