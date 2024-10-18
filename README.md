# Lab4_team
### КНз-31с

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.
We've created requirements.txt with all libraries that we are going to use,
so to run the code you will need to install all dependencies from there.
```bash
pip install -r reqirements.txt
```


# Created by Ruslan Konoz

### dotenv
Dotenv is a Python library for dealing with environment variables.
## Usage

```python
import os
from dotenv import load_dotenv, dotenv_values

# load all the env variables
load_dotenv()

# gets the desired variable
os.getenv("<variable_name>")
```


