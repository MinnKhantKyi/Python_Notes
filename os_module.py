import os

# getcwd = get current working directory(Folder)
# print(os.getcwd())
# print()

# chdir = change directory
# os.chdir("C:\\Users\\Acer\\Desktop")
# print(os.getcwd())
# print()

# directory list in directory
# print(os.listdir())
# print()

# make directory
# os.mkdir("os module")
# print(os.listdir())
# print()

# make directory by tree structure
# os.makedirs("os_module_1\\mkdir\\makedirs")

# remove directory
# os.rmdir("os module")

# remove directory and all directories in it
# os.removedirs("os_module_1\\mkdir\\makedirs")

# rename directory
# os.mkdir("Test")
# os.rename("Test", "Test_2")

# path = os.getcwd()

# get access to directory and all of its directories and files
# tuple unpacking
# (str, list, list)
# for dirpath, dirname, files in os.walk(path):
#    print()
#    print(f"Current Directory Path - {dirpath}")
#    print(f"Current Directory - {dirname}")
#    print(f"Files - {files}")
#    print()

# get environment variable
# path = os.environ.get("PATH")
# print(path)

# Join two paths
# path = os.getcwd()
# second_path = "Minn Khant Kyi_Assignment_4"
# final_path = os.path.join(path, second_path)
# print(final_path)

# basename and directory name of a directory path
path = os.getcwd()
print(path)
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))

# check dir path exits or not
print(os.path.exists(path))

# check it is dir path or not
print(os.path.isdir(path))

# check it is file or not
# file extension (eg - text.txt) must include
print(os.path.isfile("C:\\Users\\Acer\\Desktop\\pythonNis\\Content_Assignment4.txt"))