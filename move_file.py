import os
import shutil
from_dir="/Users/shauryakumar/Documents/Document_Files"
to_dir="/Users/shauryakumar/Desktop/Project102"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,ext=os.path.splitext(file_name)
    print(name,ext)
    if ext==" ":
        continue
    if ext in [".txt", ".doc", ".docx", ".pdf",".png"]:
       path1=from_dir+"/"+file_name
       path2=to_dir+"/"+"Document_files"
       path3=to_dir+"/"+"Document_files"+"/"+file_name
    if os.path.exists(path2):
       print("moving"+file_name+"....")
       shutil.move(path1,path3)
    else:
       os.makedirs(path2)
       print("moving"+file_name+"....")
       shutil.move(path1,path3)