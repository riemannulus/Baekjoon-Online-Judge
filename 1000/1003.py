import sys
dp = [(1, 0), (0, 1)]

for i in range(2, 40):
    dp.append(tuple(map(sum, zip((dp[i-2]), (dp[i-1])))))

case = int(sys.stdin.readline())

while case > 0:
    a = int(sys.stdin.readline())
    print("%d %d" % dp[a])
    case = case - 1
