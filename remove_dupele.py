inp=input().split(',')
li=[int(item) for item in inp]
newl=[]
for i in li:
    if i in newl:
        continue
    else:
        newl.append(i)
print(newl)