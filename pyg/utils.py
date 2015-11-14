from mimetypes import guess_type


"""
Basically this is a file that contains random stuff that we need but
doesn't really fit with the general scheme of the other files
"""


def detect_mimetype(file):
    return guess_type(file)
