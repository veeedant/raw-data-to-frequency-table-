from prettytable import PrettyTable

table = PrettyTable()
table.field_names=["Xi","f"]

file_input = input("enter the file adress:")
file = open(file_input,"r")

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

for i in range(len(frequency)):
	table.add_row([frequency[i][0],frequency[i][1]])

print(table)
