# Github organization repositories backup system
This is a simple script to obtain local backups of all repos in a Github organization.
---
Languages:
<p align="center">
  <span>English</span> |
  <a href="https://github.com/brosas-espinosa/Repo_organizaztions_backup_system/blob/main/language/spanish/README.spanish.md">Español</a> |
</p>

You'll need a couple of things for this script to work:
- Optional: Python virtual environment
- Requests library
- GitPython library
- Github API token
- Organization repos url
- SSH key for your account
***
## Virtual environment
To create and activate a virtual environment in Windows, you can do it by running the following commands:
```powershell
mkdir <venv-name>
python -m venv <venv-name>
Set-ExecutionPolicy Unrestricted -Scope Process
.\<venv-name>\Scripts\activate
```
Use the command `deactivate` to exit the virtual environment.

To create and activate a virtual environment in Linux, you can do it by running the following commands:
```bash
python -m venv <venv-name>
source <venv-name>/bin/activate
```
Use the command `deactivate` to exit the virtual environment.
## Python libraries
To install the necessary libraries you can do it by running the following command:
```powershell
pip install -r requirements.txt
```
## Github API token
Next, to get the Github API token, you'll need to go to your Github account settings and create a new token. Make sure to create it with the necessary permissions (repo, admin:org, etc).
## Organization repos url
To get the organization repos url, you'll need to go follow this structure:
```powershell
https://api.github.com/orgs/<organization_name>/repos
```
Note: The script is desinged to work with multiple organizations, so you can add as many as you want in the list `LIST_URLS`.
## SSH key
The ssh key is used to clone the repos, so you'll need to create one and add it to your Github account. The method will vary depending on your OS, just remember to use it before running the script.
***
## Running the script
To run the script, you'll need to run the following command:
```powershell
python backup.py
```

The files will be saved in the following structure:
```
<repositories_backup>
    <organization_name>
        <year>
            <month>
                <date>
                    <repo_name>
                        <repo_files>
```
If you want to change the backup path, you can do it by changing the variable `V_BACKUP_DIR` in the script.

