either = [1,3,5,7,9]
odd = [2,6,10]
even = [4,8]
N = int(input())
if(N>=1 and N<=10):
    if N in either:
        print("Either")
    elif N in odd:
        print("Odd")
    else:
        print("Even")