from fnmatch import filter as fn_filter
from os import walk, path
import hashlib

from utils import detect_mimetype
from github import GithubAPIManager
from languages import *


class Pygemony(object):
    """
    The main driver of pygemony, pulls the seperate pieces together.
    """
    def __init__(self, user=None, token=None, owner=None, repo=None):
        # todo_found contains a list of the following layout:
        # ['file_path', 'line_number', 'todo_message', 'md5 of todo']
        self.blacklist = ['build', '.git']
        self.todo_found = []
        self.github = GithubAPIManager(user, token, owner, repo)
        # TODO(ian): Add support for parsing more than one file type
        self.language = self.lookup_language()

    def _sanitize_todo_line(self, lines):
        """
        Strips tab, newline, and comment characters form the TODO line.

        :param str lines: The found line containing a TODO
        :rtype: str
        :return: The sanitized TODO line.
        """
        # We're mainly aiming to remove newlines and tab characters here.
        lines = lines.replace('\n', '')
        while '    ' in lines or '\t' in lines:
            lines = lines.replace('    ', '')
        for lang in self.language:
            lines = lines.replace(lang.single_comment, '')
        return lines

    @staticmethod
    def hash_todo(todo_content, file_name):
        """
        Hashes the TODO line with the file name

        :param str todo_content: The line in the file containing TODO
        :param str file_name: The file name containing the TODO line.
        :rtype: str
        :return: The MD5 hash of the `todo_content` and `file_name`
        """
        m = hashlib.md5()
        m.update('{0}-{1}'.format(todo_content, file_name))
        return str(m.hexdigest())

    def parse_for_todo(self, f, file_):
        """
        Searches (line-by-line) through a file's content and and looks for
            lines containing TODO.

        :param file_handle f: The handle to the file that is currently being
            searched
        :param str file_: The name of the file currently being searched
        """
        for i, line in enumerate(f.readlines()):
            if "TODO" in line and self._starts_with_comment(line):
                line = self._sanitize_todo_line(line)
                self.todo_found.append([file_, i, line, self.hash_todo(line, file_)])

    def parse_by_extension(self, files):
        """
        Parses the list of the directory for files with an acceptable
        extension. The extension is determined by data returned from github on
        the languages used in the project.

        :param list files: The list of all files in the current repository
        :rtype: generator(str)
        :return: Generates a list of acceptable-to-parse files.
        """
        for lang in self.language:
            for ext in lang.file_exts:
                for file_ in fn_filter(files, ext):
                    yield file_

    def find_all_files(self, root):
        """
        Walks the current repository directory and determines viable files

        :param str root: The root directory
        :rtype: list
        :return: The list of files found and determined to be viable.
        """
        files_found = []

        for roots, _, files in walk(root):
            base_dir = roots.split('/')[1]

            if base_dir not in self.blacklist:
                for file_ in self.parse_by_extension(files):
                    files_found.append(path.join(roots, file_))

        return files_found

    def file_handler(self):
        """
        Handles IO with the file

        :rtype: list
        :return: The list of files found
        """
        # First we need to remove any non-text files
        files_found = self.find_all_files('./')
        # TODO(ian): filter() over files to parse out by mimetype
        for file_ in files_found:
            file_type = detect_mimetype(file_)
            # We're looking for startswith('text/'). Mimetype returns
            # None if it can't determine file type. Remove if either is True
            try:
                if file_type[0].startswith("application") or file_type[0] is None:
                    files_found.remove(file_)
            except (AttributeError, IndexError) as e:
                print "Failed to open file {} with error of {}".format(file_, e)

        for file_ in files_found:
            try:
                with open(file_, 'r') as f:
                    self.parse_for_todo(f, file_)
            except IOError as e:
                print "Failed to open file {} with error of {}".format(file_, e)

        return files_found

    def run(self):
        """
        Starts the process of finding TODOs
        """
        self.file_handler()
        self.github.commit(self.todo_found)

    def lookup_language(self):
        """
        Constructs langauge classes based on what is found in github data.
        
        :rtype: list
        :return: A list of language classes that will be found in a github
            repo.
        """
        lang_map = {'cpp': LanguageCPP,
                    'python': LanguagePython,
                    'javascript': LanguageJavascript,
                    'c': LanguageC,
                    'go': LanguageGo,
                    'erlang': LanguageErlang}
        langs = [i for i in self.github.get_languages()]

        for i in langs:
            self.blacklist.append(lang_map[str(langs[0][0]).lower()]().ignore_dir)

        return [lang_map[str(langs[0][0]).lower()]()]

    def _starts_with_comment(self, line):
        """
        Verifies a line (containing the word TODO) starts with a comment, if it
        does, we deem it to be commit-viable.
        
        :param str line: The line that contains "TODO"

        :rtype: bool
        :return: True if line starts with a comment (is a valid TODO statement)
        """
        comments = self._create_comment_start_list()
        for comment in comments:
            if line.startswith(comment):
                return True

    def _create_comment_start_list(self):
        """
        Create a list of comments from each language class associated with the
            current repo.

        :rtype: list
        :return: A list of strings containing all line-start comments.
        """
        comments = []
        for lang in self.language:
            comments.append(lang.single_comment)
            comments.append(lang.multi_comment[0])
        return comments
