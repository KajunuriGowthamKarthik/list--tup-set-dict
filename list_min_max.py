l=[15,2,7,25,10,1000]
maxi=l[0]
mini=l[0]
for i in l:
    if i>maxi:
        maxi=i
    elif i<mini:
        mini=i
print({f"max:{maxi} min:{mini}"})