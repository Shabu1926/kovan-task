myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
lst = []
for x,y in myfamily.items():
    #print(y)
    
    for w,z in y.items():
        
        if w=='year':
            if z%2!=0:
              lst.append(y['name'])
print(lst)
