# text = "X-DSPAM-Confidence:    0.8475"
# x = text.find("0")
# vig = text[x:]
# print(float(vig))
# print("hello Users, it's Phyton data Structures")
queue = ['John', 'Amy', 'Bob', 'Adam']
while True:
    name = input()
    if name != 'stop':
        queue.append(name)
    else:
        print('programing stop and in waiting room ', len(queue), ' persons')
        break
print(queue)

