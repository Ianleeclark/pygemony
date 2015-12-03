from pyg.Pygemony import Pygemony
from pyg.utils import get_git_info


def run():
    user = raw_input("Please input your Github Username: ")
    token = raw_input("Please input your Github API Token: ")

    owner, repo = get_git_info()
    return {'user': user, 'token': token, 'owner': owner, 'repo': repo}

if __name__ == "__main__":
    args = run()

    pygemony = Pygemony(args['user'], args['token'],
                        args['owner'], args['repo'])
    pygemony.run()
