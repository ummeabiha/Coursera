fname = input("Enter file name: ")
fh = open(fname)

lst = list()

for line in fh:
    splitted_line = line.split()
    lst += (splitted_line)

list = []
for i in lst:
    if i in list:
        continue
    else:
        list.append(i)

list.sort()
print(list)
