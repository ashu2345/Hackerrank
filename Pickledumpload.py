import pickle
shoplistfile = "shoplist.txt"
shoplist = ['assassins creed','paladins','overwatch']
f = open(shoplistfile,'wb')
pickle.dump(shoplist,f)
f.close()
del shoplist
f = open(shoplistfile,'rb')
storedlist = pickle.load(f)
print(storedlist)
