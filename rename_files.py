import os

def rename_files():
    
    #(1) get file names from a folder
    
    file_list = os.listdir("/Users/Zoe/Dropbox/CS/life")
    saved_path = os.getcwd()
    os.chdir("/Users/Zoe/Dropbox/CS/life")
    
    #(2) for each files, rename filename
    
    for file_name in file_list:
        print("Old name - "+file_name)
        print("New name - "+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)

rename_files()
