# Git Basics

1. Initializing a git repo: `git init`
2. Add an untracked file: `git add file`. The same command is used to *stage* a tracked modified file. 
3. Check status: `git status`. The newly added file is in *modified* state.
4. Commit the file: `git commit -m "added file"`
5. To unstage a file `git reset HEAD file`. To unstage all files `git reset HEAD`.