name = input("Enter file:")
handle = open(name)

d=dict()
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        line=line.split()
        line=line[5]
        line=line[0:2]
        d[line]=d.get(line,0)+1

lst=[]
for value,count in d.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print(value,count)
