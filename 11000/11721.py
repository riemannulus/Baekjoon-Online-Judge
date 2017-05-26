t=input()
a=[]
if len(t) > 10:
	for i in range(int(len(t)/10)):
		a.append(t[i*10:(i+1)*10])

	a.append(t[int(len(t)/10)*10:len(t)])

else:
	a.append(t)

for i in a:
	print(i)
