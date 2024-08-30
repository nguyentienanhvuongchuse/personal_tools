import os
from os import listdir
from os.path import isfile, join

cwd = os.getcwd()
onlyfiles = [os.path.join(cwd, f) for f in os.listdir(cwd) if 
os.path.isfile(os.path.join(cwd, f))]
path = os.path.abspath(os.getcwd())
count = 1
print(path +  '/' + str(count))

for item in  onlyfiles:
    if ".jpg" in item: 
        loca = path + '/' + str(count) + '.jpg'
        os.rename(item, loca)
    elif  ".png" in item: 
        loca = path + '/' + str(count) + '.png'
        os.rename(item, loca)
    elif  ".jpeg" in item: 
        loca = path + '/' + str(count) + '.jpeg'
        os.rename(item, loca)
    else:
        count = count
    
    count = count +1
