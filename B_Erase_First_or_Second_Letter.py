def solve(s, k):
    w = s[:k] 
    cnt = {'a': w.count('a'), 'b': w.count('b')}  
    res = min(cnt['a'], cnt['b'])  

    for i in range(k, len(s)):
        cnt[s[i]] += 1 
        cnt[s[i - k]] -= 1  
        res = min(res, min(cnt['a'], cnt['b']))  

    return res

print(solve('aabaabaa' , 3))