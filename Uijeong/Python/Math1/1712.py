import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

if c - b <= 0:
    print(-1)
else:
    n = a // (c - b) + 1
    print(n)