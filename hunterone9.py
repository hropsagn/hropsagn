# your code goes here
n = int(input())
a = []
b = input().split()
for i in range(0,n):
	a.append(int(b[i]))
for i in range(0,n):
	for j in range(i+1,n):
		if(a[i]+a[j] == 0):
			print(a[i],a[j])
			break
