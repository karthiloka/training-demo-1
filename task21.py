l=['mix','xyz','apple','xanadu','aadvark']
l1=[]
l2=[]
for i in range(len(l)):
    s=l[i]
    if s[0] == 'x':
    	l1.append(s)
    else:
    	l2.append(s)

l1.sort()
l2.sort()
l=l1+l2
print(l)