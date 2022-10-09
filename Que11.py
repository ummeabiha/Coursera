# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

value = float(0.0)
list = []

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        finder = line.find("0")
        values = line[finder:finder + 6]
        list.append(float(values))
        value += float(values)

print("Average spam confidence:", value / len(list))
