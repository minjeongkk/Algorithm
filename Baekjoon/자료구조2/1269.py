# 2022/10/14
# 대칭 차집합

Anum, Bnum = map(int,input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A-B)+len(B-A))