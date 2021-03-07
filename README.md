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

### `pydep` commands

- `pydep` can be used by directly typing `pydep` in terminal/cmd of project directory
- For creating `pyproject.toml` file, the command `pydep pyproject` is used, which initiates a new pyproject.toml file

```
Usage: pydep pyproject [OPTIONS]

  Create pyproject.toml file for the project

Options:
  --help  Show this message and exit.
```

- For creating `requirements.txt` file for the project, the command `pydep dependency` is used, which creates a requirements.txt file if a virtual environment for the project is activated

```
Usage: pydep dependency [OPTIONS]

  Create requirements.txt file for the project, if virtual environment is
  activated

Options:
  --help  Show this message and exit.
```

- For creating `poetry.lock` dependency file from `requirements.txt`, the command `pydep convert` is used, which adds all dependencies in requirements.txt to pyproject.toml and poetry.lock file

```
Usage: pydep convert [OPTIONS]

  Create poetry.lock dependency file from requirements.txt

Options:
  --help  Show this message and exit.
```
