import sys

result =[]
temp = None
for word in sys.argv[1:]:
	if word =="-lst":
		if temp!=None:
			result.append(temp)
		temp=[]
	else:
		temp.append(int(word)**2)

result.append(temp)
print(result)
