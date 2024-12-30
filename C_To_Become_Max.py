def can_become_max(a, n, k, target):
    for i in range(n):
        min_needed = [0] * n
        min_needed[i] = target
        
        c_used = 0
        for j in range(i, n):
            if min_needed[j] <= a[j]:
                break
            
            if j + 1 >= n:
                c_used = k + 1
                break
            
            c_used += min_needed[j] - a[j]
            min_needed[j + 1] = max(0, min_needed[j] - 1)
            print(min_needed , target)
        
        if c_used <= k:
            return True
    return False

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    low, high, answer = 0, max(a) + k, 0
    while low <= high:
        mid = (low + high) // 2
        if can_become_max(a, n, k, mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    
    print(answer)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()