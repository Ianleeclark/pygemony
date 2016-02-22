[![Build Status](https://travis-ci.org/GrappigPanda/pygemony.svg?branch=master)](https://travis-ci.org/GrappigPanda/pygemony)
# Pygemony

If you're anything like me, you're lazy... and then you're forgetful.
By that I mean that you mean to write things (in the future), so you write down
a nifty little #TODO(name) (Or however you comment in your language of choice).
After that, however, you get so caught up in other things that you forget about
implementing these features later on. Not any longer!

You see, I created Pygemony so that I could run Pygemony and instantly have
the todos be created as issues on my Github page. This way, I can always know
what I forgot to implement.

Moreover, Pygemony won't spam your issues page, as it hashes and saves these
stored todos into a .pyg-submitted into your git repository.

### Running pygemony is really simple!
Naturally, the first step is to get your hands on a copy of it:

Using pip:
```python
pip install pygemony
```

Cloning from gihtub:
```
git clone https://github.com/GrappigPanda/pygemony
cd pygemony
python setup.py install
```

After you've gotten a copy, there's one more thing you need to do: Generate
a Github OAUTH token.

You can read up more about oauth tokens here:
https://help.github.com/articles/creating-an-access-token-for-command-line-use/

Okay, since you've got yourself a copy of Pygemony and an OAuth token, you're
ready to roll. Example usage of Pygemony:
```
pygemony --username USERNAME --token GITHUB_TOKEN
```

Whenever I run it, it looks like so:
```
pygemony --username GrappigPanda --token $GITHUB_TOKEN
```
(I find it nice and easy to set an environmental variable $GITHUB_TOKEN, not
necessary at all!)

Pygemony should take care of all of the extra work after this and detect where
to open the issues.

If, however, you want Pygemony to report to somewhere else, you can specify by
adding additional command-line arguments:
```
--owner: The owner of the repo (think GrappigPanda)
--repo: The repo's name (think Pygemony)
```

Whenever you inevitably run into bugs because I'm dumb and don't follow best
practices, feel free to open a Github issue and yell and scream at me. But 
please don't actually yell and scream at me because that's demotivational and 
no one wants that.

### LIVE EXAMPLES:
https://github.com/GrappigPanda/pygemony/issues

https://github.com/GrappigPanda/GithubTODOScraper/issues

As this project currently stands, I do NOT consider it complete and I consider
it in very early alpha stages. I have a list of issues available on the
project's github page [Pygemony] which I'm more
than happy to receive help with.

[Pygemony]: http://github.com/GrappigPanda/pygemony

### Languages Supported
C
C++
Python (naturally :)
Javascript

