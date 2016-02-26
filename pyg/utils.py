from __future__ import print_function
from mimetypes import guess_type
from functools import wraps

import os


class InvalidGitRepo(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

def in_git_repo(function):
    @wraps(function)
    def _wrapper(*args, **kwargs):
        if os.path.isdir("./.git"):
            return function(*args, **kwargs)
        raise InvalidGitRepo("Current directory is not a valid git repo!")
    return _wrapper


def get_git_info():
    repo = ''
    with open('.git/config') as f:
        for line in f.readlines():
            if 'url' in line:
                repo = line.replace('url = ', '').strip()
    r = repo.split('/')
    # Return a tuple containing the owner and the repo name
    return r[-2], r[-1]


def detect_mimetype(file_):
    return guess_type(file_)


@in_git_repo
def detect_curr_branch():
    with open('.git/HEAD', 'r') as f:
        try:
            return f.readline().split("heads/")[-1].strip()
        except IOError:
            raise InvalidGitRepo("Cannot locate .git/HEAD")
        except IndexError:
            raise InvalidGitRepo("Invalid HEAD file, no branch found")

