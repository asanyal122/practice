t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(arr)
    dp=[int(0) for i in range(len(arr))]
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])
    for i in range(2,len(arr)):
        dp[i]=max(dp[i-1],dp[i-2]+arr[i])

    print(dp[-1])
