from collections import Counter

def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    a=[]
    b=0
    c=1
    for i in tangerine:
        if i==b:
            c+=1
            continue
        a.append(c)
        c=1
        b=i
    a.append(c)
    del a [0]
    a.sort(reverse=True)
    c=0
    b=0
    for i in a:
        c+=i
        b+=1
        if c>=k:
            answer=b
            return b

count = sorted(Counter([1, 3, 2, 5, 4, 5, 2, 3]).items())
print(count)
print(solution(6,	[1, 3, 2, 5, 4, 5, 2, 3]))