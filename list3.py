list1={1,2,3}
list2={1,2,3,8,5,7,0}
list3=list(zip(list1,list2))
print(list3)

list1={'l','e','o','n'}
list2={1,2,3,8,5,7,0}
list3=list(zip(list1,list2))
print(list3)

lst1=[12,43,52,37]
lst2=[184,264,615,352]
for x,y in zip(lst1,lst2[::-1]):
    print(x,y)