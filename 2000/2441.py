j = int(input())
for i in reversed(range(j)):
	print(' '*(j-(i+1)) + '*'*(i+1))
