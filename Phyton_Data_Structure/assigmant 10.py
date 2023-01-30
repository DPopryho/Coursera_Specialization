name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
handle = open(name)
lst = list()
dic = dict()
for sting in handle:
    try:
        if not sting.startswith("From ") : continue
    except:
        sting.startswith("From:")
    pos = sting.find(":")
    lst.append(sting[pos - 2:pos])
for word in lst:
    dic[word] = dic.get(word, 0) + 1
newlst = list()
for k,v in dic.items():
    newtup = (k, v)
    newlst.append(newtup)
newlst = sorted(newlst)
for k,v in newlst:
    print(k,v)

