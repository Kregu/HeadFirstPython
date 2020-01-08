phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist = plist[1:8]
plist.extend([plist.pop(), plist.pop()])
plist.remove("'")
plist.insert(2, plist.pop(3))

phrase = ''.join(plist)
print(plist)
print(phrase)
