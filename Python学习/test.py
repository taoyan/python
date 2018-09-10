# def gettext():
#     txt=open("English.txt","r").read()
#     txt=txt.lower()
#     for ch in '!@#$%^&*()_+-=><?':
#         txt=txt.replace(ch," ")
#     return txt
# Englishtxt=gettext()
# letters=Englishtxt.split()
# counts={}
# for letter in letters:
#     counts[letter]=counts.get(letter,0)+1
# items=list(counts.items())
# items.sort(key=lambda x:x[1],reverse=True)
# for i in range(26):
#     word,count=items[i]
#     print("{}{1:>5}".format(word,count))


def gettext():
    txt=open("English.txt","r").read()
    txt=txt.lower()
    for ch in '!@#$%^&*()_+-=><?':
        txt=txt.replace(ch," ")
    return txt
text=gettext()

counts = {}
for char in text:
    if char >= 'a' and char <= 'z':
        counts[char] = counts.get(char,0)+1

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
print(items)