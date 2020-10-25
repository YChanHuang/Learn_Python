def solution(A):
    arr = [0] * 1000001
    for a in A:
        if a>0:
            arr[a] = 1
    for i in range(1, 1000000+1):
        if arr[i] == 0:
            return i


[(i+1) for i in range(len(a)+1) if (i+1 in a)==False][0]

def pos(a):
    A = set(a)
    return A
    ans = 1
    while ans in A:
       ans += 1
    return ans

pos([1, 3, 6, 4, 1, 2])
