def search(arr):
    global count,output
    new_arr = list(map(int,sys.stdin.readline().split()))
    new_arr[0] += arr[0]
    new_arr[-1] += arr[-1]
    output =max(output,new_arr[-1],new_arr[0])
    for n in range(1,len(new_arr)-1):
        left = new_arr[n] + arr[n-1]
        right = new_arr[n] + arr[n]
        new_arr[n] = max(left,right)
        output = max(output,new_arr[n])
    count += 1
    if count !=N:
        search(new_arr)

import sys
sys.setrecursionlimit(10**7)
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline())]

output = 0
count = 1
if N != 1:
    search(arr)
else:
    output = arr[0]

print(output)