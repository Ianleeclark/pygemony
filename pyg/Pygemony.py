from __future__ import print_function

from fnmatch import filter as fn_filter
from os import walk, path
import hashlib

from pyg.utils import detect_mimetype
from pyg.github import GithubAPIManager
from pyg.languages import *


class Pygemony(object):
    def __init__(self, user=None, token=None, owner=None, repo=None):
        # todo_found contains a list of the following layout:
        # ['file_path', 'line_number', 'todo_message', 'md5 of todo']
        self.blacklist = ['build', '.git']
        self.todo_found = []
        self.github = GithubAPIManager(user, token, owner, repo)
        # TODO(ian): Add support for parsing more than one file type
        self.language = self.lookup_language()

    def find_end_comment(self, f):
        # TODO(ian): Remove this function as we no longer support multiline TODO
        todo_content = []
        x = f
        count = 0
        for line in x.readlines():
            todo_content.append(line)
            if self.language.multi_comment[1] in line:
                return todo_content

            if count > 20:
                return None

            todo_content.append(line)
            count += 1

    def _sanitize_todo_line(self, lines):
        # We're mainly aiming to remove newlines and tab characters here.
        lines = lines.replace('\n', '')
        while '    ' in lines or '\t' in lines:
            lines = lines.replace('    ', '')
        for lang in self.language:
            lines = lines.replace(lang.single_comment, '')
        return lines

    @staticmethod
    def hash_todo(todo_content, file_name):
        m = hashlib.md5()
        m.update('{}-{}'.format(todo_content, file_name).encode('utf-8'))
        return str(m.hexdigest())

    def parse_for_todo(self, f, file_):
        for i, line in enumerate(f.readlines()):
            if "TODO" in line and self._starts_with_comment(line):
                line = self._sanitize_todo_line(line)
                self.todo_found.append([file_, i, line, self.hash_todo(line, file_)])

    def parse_by_extension(self, files):
        for lang in self.language:
            for ext in lang.file_exts:
                for file_ in fn_filter(files, ext):
                    yield file_

    def find_all_files(self, root):
        files_found = []

        for roots, _, files in walk(root):
            base_dir = roots.split('/')[1]

            if base_dir not in self.blacklist:
                for file_ in self.parse_by_extension(files):
                    files_found.append(path.join(roots, file_))

        return files_found

    def file_handler(self):
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
                print("Failed to open file {} with error of {}".format(file_, e))

        for file_ in files_found:
            try:
                with open(file_, 'r') as f:
                    self.parse_for_todo(f, file_)
            except IOError as e:
                print("Failed to open file {} with error of {}".format(file_, e))

        return files_found

    def run(self):
        self.file_handler()
        self.github.commit(self.todo_found)

    def lookup_language(self):
        lang_map = {'cpp': LanguageCPP,
                    'python': LanguagePython,
                    'javascript': LanguageJavascript,
                    'c': LanguageC,
                    'go': LanguageGo}
        langs = [i for i in self.github.get_languages()]

        for i in langs:
            self.blacklist.append(lang_map[str(langs[0][0]).lower()]().ignore_dir)

        return [lang_map[str(langs[0][0]).lower()]()]

    def _starts_with_comment(self, line):
        comments = self._create_comment_start_list()
        for comment in comments:
            if line.startswith(comment):
                return True

    def _create_comment_start_list(self):
        comments = []
        for lang in self.language:
            comments.append(lang.single_comment)
            comments.append(lang.multi_comment[0])
        return comments
