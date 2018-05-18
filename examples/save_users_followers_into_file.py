"""
    instabot example

    Workflow:
        Save users' followers into a file.
"""
import os
import sys
import argparse
from instabot import Bot
sys.path.append(os.path.join(sys.path[0], '../'))


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
parser.add_argument('filename', type=str, help="filename")
parser.add_argument('users', type=str, nargs='+', help='users')
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)

fh = open(args.filename, "a+")
for username in args.users:
    followers = bot.get_user_followers(username)
    for user in followers:
        fh.write(user + "\n")
fh.close()
