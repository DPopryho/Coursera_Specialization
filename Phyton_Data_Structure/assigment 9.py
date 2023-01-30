name = input("Enter file:")
handle = open(name)
count = dict()
for sting in handle:
    try:
        if not sting.startswith("From:"):
            continue
    except:
        sting.startswith("From")
    sting = sting.split()
    stings = sting[1]
    count[stings] = count.get(stings, 0) +1
    #print(sting)

bigcount = None
bigword = None
for word, count in count.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print (bigword, bigcount)




