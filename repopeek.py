#!/usr/bin/env python

import argparse
import math
from pathlib import Path
import sys
from typing import Any, Dict, List

import requests

try:
    from colorama import init as colorama_init
    from colorama import Fore, Back, Style
except ImportError:
    class ColoramaShim:
        def __getattribute__(self, key):
            return ''

    Fore = Back = Style = ColoramaShim()
else:
    colorama_init(autoreset=True)


parser = argparse.ArgumentParser(
    description='Provides information about a git repository hosted on '
                'GitHub without cloning it.')
parser.add_argument('GitHub_URL', type=str,
                    help='A GitHub URL for a repo to analyze')
args = parser.parse_args()


def num_kilobytes_to_size_str(size_bytes: int) -> str:
    size_name = ("KiB", "MiB", "GiB", "TiB")
    x = int(math.floor(math.log(size_bytes, 1024)))
    return f"{size_bytes / (1024 ** x):.2f} {size_name[x]}"


def get_languages(language_url: str) -> List[str]:
    languages = []
    req = requests.get(language_url).json()
    for i in req:
        languages.append(i)
    return languages


def get_license(lic: Dict[str, str]) -> str:
    for k, v in lic.items():
        if k == 'name':
            return v

def get_commits(repo_info: Dict[str, Any]) -> None:

    print(Fore.YELLOW + "\nCommit details of the repository")
    print(Fore.YELLOW + "----------------------")

    url = repo_info['commits_url'][:-6]
    req = requests.get(url).json()

    sha_list = []
    for i in req:
        for k, v in i.items():
            if k == 'sha':
                sha_list.append(v)
    
    commit = url+ "/" + sha_list[0]
    
    req = requests.get(commit).json()

    for k, v in req.items():
        if k == 'commit':
            for k,v in v.items():
                if k == 'message':
                    print("Last Commit Message: " + v)
                if k == 'committer':
                    for k,v in v.items():
                        if k == 'date':
                            commit_date = v.split('T')
                            print("Last Commit Date and Time: " + "On " + commit_date[0] + " at " + commit_date[1].replace("Z", " (UTC)"))

def print_info(repo_info: Dict[str, Any]) -> None:
    print(Fore.YELLOW + "Basic information about the repository")
    print(Fore.YELLOW + "--------------------------------------")
    print(f"Repository Name: {repo_info['name']}")
    print(f"Default Branch: {repo_info['default_branch']}")
    print(f"Repository Size: {num_kilobytes_to_size_str(repo_info['size'])}")
    print(f"Repository License: {get_license(repo_info['license'])}")
    print(f"Repository Type: Fork" if repo_info['fork'] else "Repository Type: Source")
    print(f"Repository Description: {repo_info['description']}")

    print(Fore.YELLOW + "\nLanguages used in the repository")
    print(Fore.YELLOW + "--------------------------------")
    print(*get_languages(repo_info['languages_url']), sep=', ')

    print(Fore.YELLOW + "\nRepository Statistics")
    print(Fore.YELLOW + "---------------------")
    print(f"Forks: {repo_info['forks']}")
    print(f"Watchers: {repo_info['watchers']}")
    print(f"Open Issues: {repo_info['open_issues']}")
    print(f"Total Stars: {repo_info['stargazers_count']}")

    print(Fore.YELLOW + "\nURLs of the repository")
    print(Fore.YELLOW + "----------------------")
    print("GIT:   " + Fore.BLUE + repo_info['git_url'])
    print("SSH:   " + Fore.BLUE + repo_info['ssh_url'])
    print("SVN:   " + Fore.BLUE + repo_info['svn_url'])
    print("Clone: " + Fore.BLUE + repo_info['clone_url'])

def main(args: argparse.Namespace) -> None:
    path = Path(args.GitHub_URL)
    org = path.parts[-2]
    repo_name = path.stem
    url = f'https://api.github.com/repos/{org}/{repo_name}'
    repo_info = requests.get(url).json()
    
    for i, v in repo_info.items():
        if v == 'Not Found':
            print(Fore.RED + "Error: Repository not found.", file=sys.stderr)
            exit(1)

    print_info(repo_info)
    get_commits(repo_info)
    exit(0)

if __name__ == '__main__':
    try:
        main(args)
    except KeyboardInterrupt:
        print("Keyboard Interupted")
        quit()
