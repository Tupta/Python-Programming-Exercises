import shelve, shutil
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
y=list(shelfFile.keys())
print(y)
j=list(shelfFile.values())
print(j)
shelfFile.close()