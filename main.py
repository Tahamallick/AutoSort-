import os,shutil
path = r"C:/Users/hp  uzer/Desktop/file sorter tutorials/"
dir=os.listdir(path)
#print(dir)
folder_names=["image file","text file","csv file"]
for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])


for file in dir:
    if ".csv" in file and not os.path.exists(path + "csv file/"+ file ):
        shutil.move(path +file,path + "csv file/" + file )
    elif ".txt" in file and not os.path.exists(path + "text file/"+ file ):
        shutil.move(path +file,path + "text file/" + file )
    elif ".png" in file and not os.path.exists(path + "image file/"+ file ):
        shutil.move(path +file,path + "image file/" + file )
    elif ".jpg" in file and not os.path.exists(path + "image file/"+ file ):
        shutil.move(path +file,path + "image file/" + file )




