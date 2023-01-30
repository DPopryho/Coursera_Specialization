# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
number = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.strip()
    # print(line)
    number += 1
    num = line.split(" ")
    # print(num[1])
    count += float(num[1])
    avr = count / number

print("Average spam confidence: " + str(avr))
# print("Done")

