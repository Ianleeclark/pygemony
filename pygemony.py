import argparse

from pyg.Pygemony import Pygemony

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--token', required=True)
    parser.add_argument('--username', required=True)
    parser.add_argument('--owner')
    parser.add_argument('--repo')

    args = parser.parse_args()
    args = vars(args)

    pygemony = Pygemony(args.get('username'),
                        args.get('token'),
                        args.get('owner'),
                        args.get('repo'))
    pygemony.run()
