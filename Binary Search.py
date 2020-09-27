T = int(input())
for i in range(T):
    N = int(input())
    A=list(map(int,input().split()))
    A.sort()
    S= int(input())
    l=0
    flag=0
    r=len(A)-1
    for j in range(len(A)):
        if r>=l:
            mid=l+ int((r-l)/2)
            if A[mid]==S:
                print(mid)
                flag=1
                break
            elif A[mid]>S:
                r=mid-1
            else:
                l=mid+1
        else:
            flag=0
    if flag==0:
        print("Number not found")
                    
