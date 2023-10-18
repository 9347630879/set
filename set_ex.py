#data type
#implicit
a = {'1','2','3'}
print(a)

#explicit
a = set(('1','2','3'))
print(type(a))

#data variable and annotation

a : set = {'1','2','3'}
print(type(a))

#create
#add

a : set = {'1','2','3'}
a.add('66')
print(a)

#update
a : set = {'1','2','3'}
b : set = {'d','s','s'}
a.update(b)
print(a)  #duplicates not allowed


#delete
#remove

a : set = {'1','2','3','6','100'}
a.remove('6')
print(a)

#discard
a : set = {'1','2','3','6','100'}
a.discard('p')
print(a)


#pop
a : set = {'a','f'}
a.pop()
print(a)


#union

a : set = {'1','2','3','6','100'}
b : set = {'a','f'}
s = a.union(b)
print(s)



#intersection


a : set = {'1','2','3','6','100'}
b : set = {'a','f','2','100'}
s = a.intersection(b)
print(s)
