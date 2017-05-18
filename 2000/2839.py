t = int(input())
newscore = 0
for i in range(int(t/5) + 1):
    temp = t - 5*i
    if temp % 3 == 0:
        newscore = int(temp / 3) + i
    
if newscore == 0:
    print(-1)
else:
    print(newscore)
