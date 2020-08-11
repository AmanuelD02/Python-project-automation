import os
import sys

# project creation folder
current_folder = 'D:\\CODES'
project_name = str(sys.argv[1])

# ULL PATH
_dir = current_folder + '/' + project_name


# create the project Folder
os.mkdir(_dir)
os.chdir(_dir)

os.system('git init')


os.system('code .')


