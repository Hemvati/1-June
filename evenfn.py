def evenlist():
	dfltlst=[1,2,3,4,5,6,7,8,9]
	even=[]
	for i in dfltlst:
		if (i%2==0):
			even.append(i)
	print(dfltlst)
	return(even)
evn_list=evenlist()
print(evn_list)
