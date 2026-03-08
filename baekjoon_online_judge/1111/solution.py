import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

if N == 1:
    print("A")

elif N == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print("A")

else:
    if arr[1] == arr[0]:
        if arr[2] != arr[1]:
            print("B")
        else:
            for i in range(N-1):
                if arr[i] != arr[i+1]:
                    print("B")
                    exit()
            print(arr[0])
    else:
        if (arr[2] - arr[1]) % (arr[1] - arr[0]) != 0:
            print("B")
            exit()
        
        a = (arr[2] - arr[1]) // (arr[1] - arr[0])
        b = arr[1] - arr[0] * a
        
        for i in range(N-1):
            if arr[i] * a + b != arr[i+1]:
                print("B")
                exit()
        
        print(arr[-1] * a + b)