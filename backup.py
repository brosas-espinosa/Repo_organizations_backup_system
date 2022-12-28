# Description: Script to backup all repositories from an organization in GitHub
# Note 1: For this script to work, you need to have a GitHub API key with the correct permissions, 
# an SSH key added to your GitHub account and the ssh has to be used previously at least once.
# Note 2: You need to have installed the gitpython and requests libraries
import git
import os
import requests
from datetime import datetime
# Get date for backup folder name
V_DATE = datetime.now().strftime('%Y-%m-%d')
# Get month for backup folder name
V_MONTH = datetime.now().strftime('%B')
V_YEAR = datetime.now().strftime('%Y')
# Set environment variable for GitHub API key
os.environ['GIT_TOKEN'] = 'Your-token-here'
# Create count of repos variables
V_COUNT_CLONED, V_COUNT_PULLED = 0, 0
# Make request to GitHub API to get list of repositories for organization
LIST_URLS = ['https://api.github.com/orgs/organization-name/repos']
for url in LIST_URLS:
    V_ORG_NAME = url.split('/')[-2]
    V_HEADERS = {'Authorization': f'token {os.environ["GIT_TOKEN"]}'}
    V_RESPONSE = requests.get(url, headers=V_HEADERS)
    LIST_REPOS = V_RESPONSE.json()
    # For each repository in the list, clone it to the backup folder according to the date, month and year. If it already exists, pull changes
    for repo in LIST_REPOS:
        V_REPO_NAME = repo['name']
        V_BACKUP_DIR = f'repositories_backup/{V_ORG_NAME}/{V_YEAR}/{V_MONTH}/{V_DATE}/{V_REPO_NAME}'
        try:
            print(f'Cloning {V_REPO_NAME}')
            git.Repo.clone_from(repo['ssh_url'], V_BACKUP_DIR)
            V_COUNT_CLONED += 1
        except git.exc.GitCommandError:
            print(f'WARNING: {V_REPO_NAME} already exists, pulling changes')
            git.Repo(V_BACKUP_DIR).remotes.origin.pull()
            V_COUNT_PULLED += 1
print('*'*28)
print('* Backup finished          *')
print(f'* {V_COUNT_CLONED} repositories cloned    *')
print(f'* {V_COUNT_PULLED} repositories pulled    *')
print(f'* {V_COUNT_CLONED + V_COUNT_PULLED} repositories processed *')
print('*'*28)