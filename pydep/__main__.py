'''
command-line interface
for PyDep
'''

#import libraries
import click
import os
import platform

@click.group()
def pydep():
    "Create pyproject.toml & poetry.lock dependency files from requirements.txt"

#create requirements.txt dependency file
@pydep.command()
def dependency():
    "Create requirements.txt file for the project, if virtual environment is activated"

    #if project has a virtual environment
    if (os.getenv('VIRTUAL_ENV')):

        #if requirements.txt is present
        if (os.path.isfile("./requirements.txt")):
            os.remove("requirements.txt")

        #create file of all dependencies present in virtual environment
        if (platform.system() == 'Windows'):
            os.system('pip freeze > requirements.txt')

        else:
            os.system('pip3 freeze > requirements.txt')

        print("requirements.txt file created successfully")

    else:
        print("Virtual environment not active/running")

#create pyproject.toml file
@pydep.command()
def pyproject():
    "Create pyproject.toml file for the project"

    try:
        
        if (platform.system() == 'Windows'):

            #list of all python modules
            os.system('pip list > modules.txt')

            file = open("modules.txt", "r", encoding = "utf-8")
            modules = file.read().splitlines()
            flag = False

            for module in modules:

                #replacing byte characters
                module = module.replace("\x00", "")
                #if poetry present in modules
                if "poetry" in module:

                    flag = True
                    break

            file.close()
            os.remove("modules.txt")

            #if poetry is not present, install it
            if (flag == False):
                os.system('pip install poetry')

        else:

            os.system('pip3 list > modules.txt')

            file = open("modules.txt", "r", encoding = "utf-8")
            modules = file.read().splitlines()
            flag = False

            for module in modules:

                #replacing byte characters
                module = module.replace("\x00", "")
                if ("poetry" in module):

                    flag = True
                    break

            file.close()
            os.remove("modules.txt")

            if (flag == False):
                os.system('pip3 install poetry')

    except:
        pass

    #initiate pyproject.toml file
    os.system('poetry init')

@pydep.command()
def convert():
    "Create poetry.lock dependency file from requirements.txt"

    #if requirements.txt file is present
    if (os.path.isfile("./requirements.txt")):

        file = open("requirements.txt", "r", encoding = 'utf-8')
        modules = file.read().splitlines()

        if (len(modules) == 0):
            print("No dependencies present in requirements.txt")

        else:

            #add each module in poetry.lock file
            for module in modules:

                #replacing byte characters
                module = module.replace("\x00", "")
                dependency = module.partition('==')

                #adding dependency in poetry.lock file
                os.system(f'poetry add {dependency[0]}')

        file.close()

    else:
        print("requirements.txt file not found")

@pydep.command()
def info():
    "Information about PyDep project"

    #basic information about PyDep project
    data = [
        'PyDep is an open-sourced command-line interface, used for creating poetry dependency files from requirements.txt',
        'Source code for PyDep is available on GitHub, and it is hosted on PyPi',
        'https://github.com/Devansh3712/PyDep'
    ]

    for info in data:
        print(info)

#run the command-line interface
if __name__ == "__main__":
    pydep(prog_name = "pydep")

'''
PyDep
Devansh Singh, 2021
'''