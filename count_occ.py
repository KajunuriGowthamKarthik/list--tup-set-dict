li=[int(item) for item in input(" ").split(" ")]
n=int(input("enter num to find its count:"))
c=0
for i in li:
    if i==n:
        c+=1
print("count of",n,"is :",c)

        