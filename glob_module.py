import glob
myfiles = glob.glob("files/*.txt")

for files in myfiles:
    with open(files,'r') as file:
        print(file.read())

    
