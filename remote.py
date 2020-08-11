import os
import sys
from github import Github

# project creation folder
current_folder = 'D:\\CODES'
project_name = str(sys.argv[1])

# ULL PATH
_dir = current_folder + '/' + project_name


#Github username and Password
TOKEN =  os.environ.get('GITHUB_TOKEN')



# Connect to Github
g = Github(TOKEN)
user = g.get_user()
login = user.login

# create repo in github
repo = user.create_repo(project_name)

# Commands to create local REpository and push it to github
commands = ['git init',
        f'git remote add origin https://github.com/{login}/{project_name}.git',
        'git push -u origin master']

# create the project Folder
os.mkdir(_dir)
os.chdir(_dir)

for c in commands:
    os.system(c)


os.system('code .')






