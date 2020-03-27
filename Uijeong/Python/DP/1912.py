import sys
input = sys.stdin.readline


def continued_sum():
    dp[0] = arr[0]
    for i in range(1, n):
        if dp[i-1] >= 0:
            dp[i] = dp[i-1] + arr[i]
        else:
            dp[i] = arr[i]
    return max(dp)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * n
    print(continued_sum())