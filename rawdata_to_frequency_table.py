file_input = input("enter the file adress:")
file = open(file_input,"r")
na = "/Users/vedantarora/Documents/rawdata.txt"
data = file.read().split()

arr = []
frequency = []
for i in data:
	if i not in arr:
		arr.append(i)
		freq = data.count(i)
		frequency.append([i,freq])
for i in frequency:
	if i[0]==' '  or i[0]=='\n':
		frequency.remove(i)

print("x"," "*5,"|"," "*5,"f")
print("")
for j in frequency:
	print(j[0],"	|	",j[1])
table = {}
for x in frequency:
	table[x[0]]= x[1]
print(table)