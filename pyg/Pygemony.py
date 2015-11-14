from fnmatch import filter
from os import walk, path
import hashlib

from utils import detect_mimetype
from github import GithubAPIManager
from languages import *


class Pygemony:
    def __init__(self, language):
        # todo_found contains a list of the following layout:
        # ['file_path', 'line_number', 'todo_message', 'md5 of todo']
        self.todo_found = []
        self.language = language

    def find_end_comment(self, f):
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
        # for line in lines
        lines = lines.replace('\n', '')
        # for char in line:
        while '    ' in lines or '\t' in lines:
            lines = lines.replace('    ', '')
        return lines

    @staticmethod
    def hash_todo(todo_content):
        m = hashlib.md5()
        m.update(todo_content)
        return str(m.hexdigest())

    def parse_for_todo(self, f, file_):
        for i, line in enumerate(f.readlines()):
            if "TODO" in line:
                line = self._sanitize_todo_line(line)
                self.todo_found.append([file_, i, line,
                                        self.hash_todo(line)])
            elif "TODO" in line and self.language.multi_comment[0]:
                todo_content = self.find_end_comment(f)
                if todo_content:
                    self.todo_found.append([file_, i, line,
                                            self.hash_todo(todo_content)])

    def parse_by_extension(self, files):
        for ext in self.language.file_exts:
            for file_ in filter(files, ext):
                yield file_

    def find_all_files(self, root):
        files_found = []
        for roots, dirs, files in walk(root):
            for file_ in self.parse_by_extension(files):
                files_found.append(path.join(roots, file_))
        return files_found

    def file_handler(self):
        # First we need to remove any non-text files
        files_found = self.find_all_files('./')
        print files_found
        for file_ in files_found:
            file_type = detect_mimetype(file_)
            # We're looking for startswith('text/'). Mimetype returns
            # None if it can't determine file type. Remove if either is True
            if file_type[0].startswith("application") or file_type[0] is None:
                files_found.remove(file_)

        for file_ in files_found:
            try:
                with open(file_, 'r') as f:
                    self.parse_for_todo(f, file_)
            except IOError as e:
                print "Failed to open file {} with error of: {}".format(file_,
                                                                        e)

        return files_found

    def run(self, user, token, owner, repo):
        self.file_handler()

        github = GithubAPIManager(user, token, owner, repo)

        github.commit(self.todo_found)

if __name__ == "__main__":
    language = LanguagePython()
    pygemony = Pygemony(language)
    pygemony.run()
