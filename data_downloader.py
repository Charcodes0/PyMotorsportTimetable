# Script to download requested files from https://github.com/sportstimes/f1/tree/main/_db to Local
# Credit to @rdash99 for the base of this code

import os
from github import Github

from git_download import download_folder

repository = 'sportstimes/f1'
year_path = '/2025.json'
directory = ''

# To only be run once, on file start
def instantiate_directory ():
    # obtain the current working directory
    cwd = os.getcwd()

    # find the directory to download to
    dld = cwd + '\DataFiles'

    # check download directory exists, create if not
    ensure_folder_exists(dld)

    # change the working directory to the download folder
    os.chdir(dld)

    global directory
    directory = dld

# Requests a download of only the necessary file
def download_series(series : str):
    git = Github()
    repo = git.get_repo(repository)

    folder = '_db/' + series + year_path

    download_folder(repo, folder, directory)

def ensure_folder_exists(_dir):
    if not os.path.exists(_dir):
        print("INFO: Creating download folder")
        os.makedirs(_dir)