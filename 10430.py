ar = list(map(int, input().split()))
print((ar[0]+ar[1])%ar[2], ((ar[0]%ar[2])+(ar[1]%ar[2]))%ar[2], (ar[0]*ar[1])%ar[2], ((ar[0]%ar[2])*(ar[1]%ar[2]))%ar[2], sep="\n")
