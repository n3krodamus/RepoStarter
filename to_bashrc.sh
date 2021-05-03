##
## Added for RepoStarter
##
function create() {
    source ~/etc/.env_create
    cd
    python bin/create.py $1
    cd $PROY_FILEPATH$1
    git init
    git remote add origin git@github.com:$USERNAME_GIT/$1.git
    touch README.md
    touch .gitignore
    git add .
    git commit -m "Initial commit, from RepoStarter"
    git branch -M main
    git push -u origin main
}

