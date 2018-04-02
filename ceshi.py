a=[1,2,3,4,5]
b=[]
xvel=10
for i in range(len(a)-1):
	b.append(a[i])
b.insert(0,xvel)
print(b)