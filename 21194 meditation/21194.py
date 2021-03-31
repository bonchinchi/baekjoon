n,k = map(int,input().split())
if(n<=100000 and n>=1 and k<=n and 1<=k):
    values = [int(input()) for _ in range(n)]
    if (min(values)>=0 and max(values)<=10000 and len(values)==n):
        values.sort(reverse=True)
        answer = sum(values[:k])
        print(answer)
    else:
        pass