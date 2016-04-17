from mimetypes import guess_type

def get_git_info():
    """
    Parses the git info and returns a tuple containg the owner and repo

    :deprecated:
    :rtype: tuple
    :return: (owner name, repo name)
    """
    repo = ''
    with open('.git/config') as f:
        for line in f.readlines():
            if 'url' in line:
                repo = line.replace('url = ', '').strip()
    r = repo.split('/')
    # Return a tuple containing the owner and the repo name
    return r[-2], r[-1]


def detect_mimetype(file_):
    """
    Detects the provided file's mimetype. Used to determine if we should read
        the file line-by-line.

    :param str file_: The name of the file to guess the mimetype of
    :rtype: str
    :return: The mimetype of the file provided
    """
    return guess_type(file_)
