f = open("nc-output","r")
p=f.read()
f.close()
#print(p)

print(type(p))
#int(p)
p2=p.split()
#print(p2)
#print(int(p2[0]))

result=[]
for i in range(len(p2)):
    result.append(chr(int(p2[i])))
print("".join(result))
