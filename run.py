import os
import sys

os.system('cls')

txtfile = open(r'path to txt file', 'r+') #create an empty text file, add path
DIRECTORY_PATH = r'path to Python folder' #add path to your master projects folder

exclude = []
for root, dirs, files in os.walk(DIRECTORY_PATH):
    for dir in dirs:
        if dir.startswith(".") or dir == "__pycache__":
            exclude.append(dir)

folders = []
for root, dirs, files in os.walk(DIRECTORY_PATH):
    for folder in exclude:
        if folder in dirs:
            dirs.remove(folder)
    for dir in dirs:
            folders.append(dir)

pyfolders = []
for folder in folders:
    contains_py = False
    for root, dirs, files in os.walk(DIRECTORY_PATH + "\\" + folder):
        for file in files:
            if file.endswith("py"):
                contains_py = True
    if contains_py == True:
        pyfolders.append(folder)

padding = 3
lines = txtfile.readlines()
mostrecent = []
mostrecent.append([lines[-1].strip(), lines[-2].strip()])
mostrecent.append([lines[-3].strip(), lines[-4].strip()])
mostrecent.append([lines[-5].strip(), lines[-6].strip()])
alpha = {"a":1, "b":2, "c":3}

num = 1
print("\n____________________ RECENT ____________________\n")
for recent in mostrecent:
    spaces = len(str(len(pyfolders))) + padding - len(str(num))
    print(list(alpha.keys())[num-1], end="")
    for _ in range(spaces):
        print(" ", end="")
    print(recent[1])
    num += 1

print("____________________ FOLDERS ____________________\n")

num = 1
for pyfolder in pyfolders:
    spaces = len(str(len(pyfolders))) + padding - len(str(num))
    print(num, end="")
    for _ in range(spaces):
        print(" ", end="")
    print(pyfolder)
    num += 1

print("_________________________________________________\n")

ui = input("Enter: ")
os.system('cls')
if str(ui).isdigit():
    ui = int(ui)
    folder = pyfolders[ui-1]
    os.system(f'title {folder}')
    pyfiles = []
    for root, dirs, files in os.walk(DIRECTORY_PATH + "\\" + folder):
        for file in files:
            if file.endswith("py"):
                pyfiles.append([file, root])

    padding = 2
    num = 1
    print("\n_____________________ FILES _____________________\n")
    for pyfile in pyfiles:
        print(num, end="")
        spaces = len(str(len(pyfiles))) + padding - len(str(num))
        for _ in range(spaces):
            print(" ", end="")
        print(pyfile[0])
        num += 1
    print("_________________________________________________\n")

    ui = int(input("Enter: "))

    os.system('cls')

    print('\n')
    cd = pyfiles[ui-1][1].replace("C:\\" ,"")
    filename = pyfiles[ui-1][0]
    os.system(f'title {filename}')
    updatedfile = f'{filename.strip()}\n{cd.strip()}\n' + txtfile.read()
    txtfile.write(updatedfile)
    os.system(f'cd \\ && cd {cd} && python {filename}')
    txtfile.close()

elif ui.isalpha():
    n = alpha[ui]
    cd = mostrecent[n-1][0]
    filename = mostrecent[n-1][1]
    os.system(f'title {filename}')
    os.system(f'cd \\ && cd {cd} && python {filename}')

end = input("Press Any Key to End Program: ")
sys.exit()
