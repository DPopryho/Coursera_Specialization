# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Invalid file ")
    quit()
for upreg in fh:
    upreg = upreg.strip()
    print(upreg.upper())
