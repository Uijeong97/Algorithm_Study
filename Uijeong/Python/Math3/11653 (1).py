import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    p = 2
    while 1:
        if n == 1: break
        if n % p: p += 1
        else: print(p); n //= p