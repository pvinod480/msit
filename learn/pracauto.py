import os
g=os.walk(os.getcwd())
for dir_path,directory_name,file_names in g:
    for filename in file_names:
        if filename.endswith(".py"):
            print(os.path.join(dir_path,filename))

for py_file in python_files:
    print(py_file)
            

