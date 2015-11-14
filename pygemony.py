#!/usr/bin/env python
__author__ = 'Ian'

import argparse
from pyg.Pygemony import Pygemony
from pyg.languages import LanguageCPP, LanguagePython
import os
"""
parser = argparse.ArgumentParser(
    description="Pygemony: Parse your local github repo to find any TODO and"
                "Automagically create issues reflecting these TODOs on Github")

parser.add_argument('-u', action='store', dest='user',
                    help="Your github user")
parser.add_argument('-t', action='store', dest='token',
                    help="Your github API token")
parser.add_argument('--owner', '-o', action='store', dest='owner',
                    help="The Remote Repo's owner")
parser.add_argument('--repo', '-r', action='store', dest='repo',
                    help="The remote repo's name")
parser.add_argument('--lang', '-l', action='store', dest='lang',
                    help="Your project's language")

parser.print_help()
"""

def language_lookup(lang):
    if lang is not None:
        langs = {'cpp': LanguageCPP,
                 'python': LanguagePython}

        print langs.get(lang)
        return langs.get(lang)()
    else:
        return None

user = raw_input("Please input your username: ")
token = raw_input("Please input your token: ")
owner = raw_input("Please input your owner: ")
repo = raw_input("Please input your repo: ")
lang = raw_input("Please input your language. ")

language = language_lookup(lang)
if language is not None:
    pygemony = Pygemony(language)
    pygemony.run(user, token, owner, repo)
