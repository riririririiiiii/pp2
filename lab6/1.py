#ex1
import os
path = 'C:\\Users\\HomePC\\Desktop\\githowto'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])

#ex2
import os
print('Exist:', os.access('C:\\Users\\HomePC\\Desktop\\summary.docx', os.F_OK))
print('Readable:', os.access('C:\\Users\\HomePC\\Desktop\\summary.docx', os.R_OK))
print('Writable:', os.access('C:\\Users\\HomePC\\Desktop\\summary.docx', os.W_OK))
print('Executable:', os.access('C:\\Users\\HomePC\\Desktop\\summary.docx', os.X_OK))

#ex3
import os

def test_path_exists(path):
    print("Test a path exists or not:")
    print(os.path.exists(path))

    if os.path.exists(path):
        print("\nFile name of the path:")
        print(os.path.basename(path))
        print("\nDir name of the path:")
        print(os.path.dirname(path))

path1 = 'g:/testpath/a.txt'
path2 = 'g:/testpath/p.txt'

test_path_exists(path1)
test_path_exists(path2)

#ex4
with open(r"file.txt", 'r') as file:
	lines = len(file.readlines())
	print('Total Number of lines:', lines)

#ex5
def write_list_to_file(file_path, input_list):
        with open(file_path, 'w') as file:
            for item in input_list:
                file.write(item + '\n')

items = ['Banana', 'Mango', 'Apple', 'Strawberry']
file_path = 'items.txt'  
write_list_to_file(file_path, items)
	
#ex6
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)

#ex7
from shutil import copyfile

copyfile('23.py', '54.py')

#ex8
import os

def delete_file(file_path):
    if os.access(file_path, os.F_OK):  
        if os.access(file_path, os.W_OK):  
            os.remove(file_path) 
            print(f"File '{file_path}' has been deleted successfully.")
        else:
            print(f"Error: No write access to '{file_path}'.")
    else:
        print(f"Error: File '{file_path}' does not exist.")

file_path = 'items.txt'  
delete_file(file_path)






