t=int(input())

for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    max_=max(b-k for b in a)
    min_=min(b+k for b in a)

    if max_ > min_:
        print(-1)
    else:
        print(min_)

   
 

