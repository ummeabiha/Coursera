fname = input("Enter file:")
file = open(fname)

lst = list()

for lines in file:
    if not lines.startswith("From:"):
        continue
    else:
        lines = lines.split()
        lst.append(lines[1])

counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print (bigword,bigcount)
