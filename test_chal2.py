def solution(l, t):
    for start in range (len(l)):
        for end in range(start+1,len(l) +1):
            if sum(l[start:end])==t:
                return [start,end-1]
    return [-1,-1]
lst = [1, 2, 3, 4, 5]
print(len(lst))
T = 18
l= solution(lst, T)
print(l)
