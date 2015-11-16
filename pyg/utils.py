from mimetypes import guess_type

"""
Basically this is a file that contains random stuff that we need but
doesn't really fit with the general scheme of the other files
"""


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
