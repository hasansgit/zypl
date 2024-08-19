thisdict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : 1964
}
print(thisdict)
print(thisdict['brand'])
print(thisdict['year'])
print(len(thisdict))
print(type(thisdict))

newdict = dict.copy(thisdict)
newdict['newkey'] = 1234
print(thisdict)
print(newdict)
print(len(newdict))
newdict.clear()
print(newdict)
