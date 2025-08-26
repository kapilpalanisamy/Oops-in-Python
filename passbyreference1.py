def change(l):
    print(id(l))
    l.append(5)
    print(id(l))

l1=[1,2,3,4]
print(id(l1))
print(l1)

#cloning
change(l1[:])

print(l1)
