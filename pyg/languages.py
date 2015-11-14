__author__ = 'Ian'


class LanguageCPP:
    def __init__(self):
        self.single_comment = '//'
        self.multi_comment = ['/*', '*/']
        self.file_exts = ['*.cpp', '*.cxx', '*.c', '*.hpp', '*.hxx', '*.h']


class LanguagePython:
    def __init__(self):
        self.single_comment = '#'
        self.multi_comment = ['"""', '"""']
        # How does iron python, stackless, &c do it?
        self.file_exts = ['*.py']

