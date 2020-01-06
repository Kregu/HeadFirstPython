phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
new_list = []

remove_list = ["D", "'", "n", "i", "c", "!"]
for i in remove_list:
    plist.remove(i)

print_list = [0, 5, 2, 1, 4, 3]
for i in print_list:
    new_list.append(plist[i])

new_phrase = ''.join(new_list)
print(plist)
print(new_phrase)
