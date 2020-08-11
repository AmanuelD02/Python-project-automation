import os
import sys


# create the folder
current_folder = 'D:\\CODES'
project_name = str(sys.argv[1])


try:
    local = str(sys.argv[2])

except:
    local =''

# URL PATH
_dir = current_folder + '/' + project_name

# create the project Folder
os.mkdir(_dir)
os.chdir(_dir)


print(f'{local} here it is')
# if the projet is local only
if local =="l":
    os.system('git init')
     
else:
    from github import Github

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
            f'echo "# {repo.name}" >> README.md',
            'git add .',
            'git commit -m"Intial Commit" ',
            f'git remote add origin https://github.com/{login}/{project_name}.git',
            'git push -u origin master']


    for c in commands:
        os.system(c)



# open the project in visual studio Code
os.system('code .')






