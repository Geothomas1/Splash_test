import pandas as pd;
appName = pd.read_csv("Google-Playstore.csv") 
res=appName['App Id'].tolist()

mylist=[]
for i in range(1100001,1118136):
    mylist.append(res[i])
print(mylist)