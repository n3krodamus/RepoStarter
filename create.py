import sys
import os
from github import Github

token = os.environ['TOKEN_GIT']
path = os.environ['PROY_FILEPATH']

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(folderName))

    g = Github(token)  # safer alternative, if you have an access token
    u = g.get_user()
    repo = u.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    create()
