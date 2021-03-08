from setuptools import *
from os import path
  
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
  
setup( 
        name = 'pydep-cli',
        version = '0.1.1',
        author = 'Devansh Singh', 
        author_email = 'devanshamity@gmail.com', 
        url = 'https://github.com/Devansh3712/PyDep', 
        description = 'Create pyproject.toml & poetry.lock dependency files from requirements.txt', 
        long_description = long_description, 
        long_description_content_type = "text/markdown", 
        license = 'MIT',
        packages = find_packages(),
        include_package_data = True,
        entry_points = {
        	"console_scripts": [
        		"pydep=pydep.__main__:pydep",
        	]
        },
        classifiers = [
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ],
        install_requires = ["click==7.1.2"],
)