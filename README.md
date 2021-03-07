# PyDep
Create `pyproject.toml` & `poetry.lock` dependency files from `requirements.txt`

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>

## Installation
`pydep` can be installed in the following ways:

### Cloning the repository

- Clone this repository to your local machine

```console
git clone https://github.com/Devansh3712/PyDep.git
```

- Install `pydep` by running `setup.py` in `PyDep` directory

> Windows

```cmd
python setup.py install
```

> Linux

```console
python3 setup.py install
```

### Installing as a pip package

- Using terminal/cmd to install `pydep`

> Windows

```cmd
pip install pydep-cli
```

> Linux

```console
pip3 install pydep-cli
```

## Usage

```
Usage: pydep [OPTIONS] COMMAND [ARGS]...

  Create pyproject.toml & poetry.lock dependency files from requirements.txt

Options:
  --help  Show this message and exit.

Commands:
  convert     Create poetry.lock dependency file from requirements.txt
  dependency  Create requirements.txt file for the project, if virtual...
  pyproject   Create pyproject.toml file for the project
  ```
