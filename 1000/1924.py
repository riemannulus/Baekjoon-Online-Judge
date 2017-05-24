def f(x):
	return {
		1: 'MON',
		2: 'TUE',
		3: 'WED',
		4: 'THU',
		5: 'FRI',
		6: 'SAT',
		0: 'SUN',
	}.get(x, 'NULL')


x, y = map(int, input().split())
mon = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = y
for i in range(x):
	day = day + mon[i]
print(f(day%7))
