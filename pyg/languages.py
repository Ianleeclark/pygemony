__author__ = 'Ian'


class LanguageCPP(object):
    def __init__(self):
        self.single_comment = '//'
        self.multi_comment = ['/*', '*/']
        self.file_exts = ['*.cpp', '*.cxx', '*.c', '*.hpp', '*.hxx', '*.h']
        self.ignore_dir = []


class LanguageC(object):
    def __init__(self):
        self.single_comment = '//'
        self.multi_comment = ['/*', '*/']
        self.file_exts = ['*.c', '*.h']
        self.ignore_dir = []


class LanguagePython(object):
    def __init__(self):
        self.single_comment = '#'
        self.multi_comment = ['"""', '"""']
        # How does iron python, stackless, &c do it?
        self.file_exts = ['*.py']
        self.ignore_dir = []


class LanguageJavascript(object):
    def __init__(self):
        self.single_comment = '//'
        self.multi_comment = ['/*', '*/']
        self.file_exts = ['*.js', '.node']
        self.ignore_dir = ['node_modules']
        self.ignore_dir = []

class LanguageGo(object):
    def __init__(self):
        self.single_comment = '//'
        self.multi_comment = ['/*', '*/']
        self.file_exts = ['*.go']
        self.ignore_dir = []

