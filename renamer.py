import os

path = os.getcwd() + '/video'
print('введите путь:')

os.chdir(input())

for file in os.listdir():
    if file.__contains__('.tif') and len(file[:-5])<3:
        new_file = '0'*(2-len(file[:-5]))+file
        os.rename(file,new_file)