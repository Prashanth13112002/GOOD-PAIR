def good_pair(arr,k):
   length=len(arr)
   for i in range (length):
       #To avoid repeated addition i+1 is used here
        for j in range(i+1,length):
            if arr[i]+arr[j]==k:
                return 1
   return 0
a=list(map(int,input().split()))
b=int(input())
print(good_pair(a,b))