import pickle
file=open("configw","rb")
a=pickle.load(file)
file.close()
#print(a)
b={'a':'b','c':'d'}
print(len(b))