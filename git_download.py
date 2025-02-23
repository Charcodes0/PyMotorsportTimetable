# Script to handle the downloading of requested files
# Credit to @rdash99 for the base of this code

import os
from github import Repository, ContentFile
import requests

def download_folder(repo: Repository, folder: str, out: str):
    contents = repo.get_contents(folder)
    download(contents, out)

def download(c: ContentFile, out: str):
    r = requests.get(c.download_url)
    output_path = f'{out}/{c.path}'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as f:
        print(f'downloading {c.path} to {out}')
        f.write(r.content)

