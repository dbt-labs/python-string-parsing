# demo-python-blog

## Prerequisites

Verify that both `python3` and `git` are installed and available:
```shell
python3 --version
git --version
```

## Clone

Clone this repo using your method of choice:

<details open>
<summary>SSH</summary>

```shell
git clone git@github.com:dbt-labs/demo-python-blog.git
cd demo-python-blog
```

</details>

<details>
<summary>HTTPS</summary>

```shell
git clone https://github.com/dbt-labs/demo-python-blog.git
cd demo-python-blog
```

</details>

<details>
<summary>GitHub CLI</summary>

```shell
gh repo clone dbt-labs/demo-python-blog
cd demo-python-blog
```

</details>

## Install
Create a virtual environment and install dependencies:

<details open>
<summary>POSIX bash/zsh</summary>

```shell
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
source env/bin/activate
```

</details>

<details>
<summary>POSIX fish</summary>

```shell
python3 -m venv env
source env/bin/activate.fish
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
source env/bin/activate.fish
```
</details>

<details>
<summary>POSIX csh/tcsh</summary>

```shell
python3 -m venv env
source env/bin/activate.csh
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
source env/bin/activate.csh
```
</details>

<details>
<summary>POSIX PowerShell Core</summary>

```shell
python3 -m venv env
env/bin/Activate.ps1
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
env/bin/Activate.ps1
```
</details>

<details>
<summary>Windows cmd.exe</summary>

```shell
python -m venv env
env\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
env\Scripts\activate.bat
```
</details>

<details>
<summary>Windows PowerShell</summary>

```shell
python -m venv env
env\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
env\Scripts\Activate.ps1
```
</details>


## Run
Build the project:
```shell
dbt build
```

## Query

Examine the output:
```
duckcli demo.duckdb --table --execute "select id, transaction_time, parsed_transaction_time from transactions order by id"
```

## Wrap up
Deactivate the virtual environment when finished:

```shell
deactivate
```
