import pathlib
import os
from string import ascii_uppercase

path = '.'

# 1. Write a Python program to list only directories, files and all directories, files in a specified path.


def listDirs(p):
    print("Directories: ")
    print([x.name for x in os.scandir(path=p) if x.is_dir()])


def listFiles(p):
    print("Files: ")
    print([x.name for x in os.scandir(path=p) if x.is_file()])


def listDirsAndFiles(p):
    print("Directories and files: ")
    print([x.name for x in os.scandir(path=p)])


print("Task 1")
listDirs(path)
listFiles(path)
listDirsAndFiles(path)
print("--------------------------------------------------")

# 2. Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path


def check(p):
    exist_status = os.access(path=p, mode=os.F_OK)
    print(f'Existence : {exist_status}')
    read_status = os.access(path=p, mode=os.R_OK)
    print(f'Readibility : {read_status}')
    write_status = os.access(path=p, mode=os.W_OK)
    print(f'Writability : {write_status}')
    exec_status = os.access(path=p, mode=os.X_OK)
    print(f'Executability : {exec_status}')


print('Task 2')
check(path)
print("--------------------------------------------------")

# 3. Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.


def test(p):
    exist_status = os.access(path=p, mode=os.F_OK)
    if exist_status:
        print(f'File: {os.path.basename(p)}')
        print(f'Directory: {os.path.dirname(p)}')
    else:
        print("The file does not exist")


print("Task 3")
test('README.md')
print("--------------------------------------------------")

# 4. Write a Python program to count the number of lines in a text file.


def count(p):
    with open(p, 'r') as f:
        return len(f.readlines())


print("Task 4")
print(f'Number of lines = {count("demo.txt")}')
print("--------------------------------------------------")

# 5. Write a Python program to write a list to a file.


def show(fname, l):
    with open(fname, 'w') as f:
        f.write(str(l) + '\n')

    with open(fname, 'r') as f:
        print(f.read())


print("Task 5")
l = str(input())
show('demo.txt', l)
print("--------------------------------------------------")

# 6. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt


def generateFiles():
    for i in ascii_uppercase:
        with open(f'{i}.txt', 'w') as f:
            f.write(f'{i}\n')


print("Task 6")
generateFiles()
print("--------------------------------------------------")

# 7. Write a Python program to copy the contents of a file to another file


def copyContent(i, t):
    with open(i, 'r') as f:
        with open(t, 'w') as f2:
            f2.write(f.read())

    with open(t, 'r') as f:
        print(f.read())
    print("Copied!")


print("Task 7")
copyContent('test.txt', 'demo.txt')
print("--------------------------------------------------")

# 8. Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.


def delete(p):
    if os.access(path=p, mode=os.F_OK):
        os.remove(p)
        print("Deleted!")
    else:
        print("The file does not exist")


p = "test.txt"
print("Task 8")
delete(p)
