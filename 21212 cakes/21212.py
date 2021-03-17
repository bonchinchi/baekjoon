first = int(input())
i = 0
list = []
outputval = 0
if(first>0 and first<11):
    while(i<first):
        i+=1
        f, s = map(int, input().split())
        list.append(int(s/f))
    if (min(list)<0):
        print(0)
    else:
        print(min(list))