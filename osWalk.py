import os

for currentDir, listofdirs, listoffiles in os.walk("."):
    print("[*] Current Directory is: ", currentDir)
    print("            has directories: ", listofdirs)
    print("            has files: ", listoffiles)
    
