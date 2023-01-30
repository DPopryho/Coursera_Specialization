fname = input("Enter file name: ")
fh = open(fname)

count = 0
for line in fh:
    line = line.rstrip()
    try:
        if not line.startswith("From:"):
            continue
    except:
        line.startswith("From")
    line = line.split()
    count += 1
    print(line[1])
print("There were", count, "lines in the file with From as the first word")
