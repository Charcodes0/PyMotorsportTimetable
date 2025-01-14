# Script to download requested files from https://github.com/sportstimes/f1/tree/main/_db to Local
# Credit to @rdash99 for the base of this code

import os
import subprocess
from github import Github, Repository, ContentFile

import gitdownload

repository = 'sportstimes/f1'
year_path = '/2025.json'
directory = ''

# To only be run once, on file start
def instantiate_directory ():
    # obtain the current working directory
    cwd = os.getcwd()

    # find the directory to download to
    dld = cwd + '\DataFiles'

    # change the working directory to the download folder
    os.chdir(dld)

    global directory
    directory = dld

# Requests a download of only the necessary file
def download_series(series : str):
    git = Github()
    repo = git.get_repo(repository)

    folder = '_db/' + series + year_path

    gitdownload.download_folder(repo, folder, directory)
