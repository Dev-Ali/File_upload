#This program is created by Dev Ali
#The purpose of this program is to demonstrate the modle of a file upload function

print("1. Full secure file upload")
print("2. Unrestricted file upload")
print("3. File extension bypass")
print()
selector = int(input("What would you like to demonstrate?"))

#This function filters unintented file from being uploaded and only allows image files to get uploaded
#The function also restricts double file extensions being used as this is a great way to bypass file filters implemented on the client-side control
if selector == 1:
    file = input("Enter a filename: ")
    crr_ext = ("png", "jpg", "gif")
    split = file.split(".")
    if len(split) == 2:
        if split[1] in crr_ext:
            print("File uploaded sucessfully")
        elif split[1] not in crr_ext:
            print("File format not supported")
    elif len(split) > 2:
        print("Invalid file")

#The following function is vulnerable to unauthenticated file upload.
#The function  allows the user to upload any type of file
#A mallicous actor can take advantage of this bad practice and can upload a dangerous file (Webshell, reverse shell, etc)
elif selector == 2:
    file = input("Enter a filename: ")
    split = file.split(".")
    if len(split) == 2:
        print("File uploaded sucessfully")
    elif len(split) > 2:
        print("Invalid file")

#In this instance the program just validates the first file extension being used
#An attacker can obfuscate a virus file by using a double extension. 
#When double exntension is used the format of the file depends upon the second extension
elif selector == 3:
    file = input("Enter a filename: ")
    crr_ext = ("png", "jpg", "gif")
    split = file.split(".")
    if split[1] in crr_ext:
        print("File uploaded sucessfully")
    elif split[1] not in crr_ext:
            print("File format not supported")

