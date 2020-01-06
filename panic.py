phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()
plist.pop(0)
plist.extend([plist.pop(), plist.pop()])
plist.remove("'")
plist.insert(2, plist.pop(3))

phrase = ''.join(plist)
print(plist)
print(phrase)
