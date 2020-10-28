import pickle
file=open("b","rb")
a=pickle.load(file)
file.close()
print(a)