import click
import os
import platform

@click.group()
def pydep():
    "Create pyproject.toml & poetry.lock dependency files from requirements.txt"

@pydep.command()
def dependency():
    "Create requirements.txt file for the project, if virtual environment is activated"

    if os.getenv('VIRTUAL_ENV'):

        if platform.system() == 'Windows':
            os.system('cmd \c "pip freeze > requirements.txt"')

        else:
            os.system('cmd \c "pip3 freeze > requirements.txt"')

        print("requirements.txt file created successfully")

    else:

        print("Virtual environment not active/running")

@pydep.command()
def pyproject():
    "Create pyproject.toml file for the project"

    try:
        
        if platform.system() == 'Windows':
            os.system('cmd \c "pip install poetry"')

        else:
            os.system('cmd \c "pip3 install poetry"')

    except:

        pass

    os.system('cmd \k "poetry init"')

@pydep.command()
def convert():
    "Create poetry.lock dependency file from requirements.txt"

    if os.path.isfile("./requirements.txt"):

        file = open("requirements.txt", "r", encoding = 'utf-8')
        modules = file.read().splitlines()

        if len(modules) == 0:

            print("No dependencies present in requirements.txt")

        else:

            for module in modules:

                module = module.replace("\x00", "")
                dependency = module.partition('==')

                os.system(f'cmd \c "poetry add {dependency[0]}"')

if __name__ == "__main__":
    pydep(prog_name = "pydep")