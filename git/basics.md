# Git Basics

## Staging / Committing
1. Initializing a git repo: `git init`
2. Add an untracked file: `git add file`. The same command is used to *stage* a tracked modified file. 
3. Check status: `git status`. The newly added file is in *modified* state.
4. Commit the file: `git commit -m "added file"`
5. To unstage a file `git reset HEAD file`. To unstage all files `git reset HEAD`.
6. If a staged file is modified, the same file will appear under *staged* and *modified*.
7. Create a new branch and switch to it : `git checkout -b branch1`.
8. See Modified unstaged changes: `git diff` (diffs modified and staged)
9. See staged changes: `git diff --staged` (diffs staged and last commit)
10. Push changes to remote: `git push`

## Commit History
1. Basic: `git log`
2. See diff of each commit and limit log history to 2: `git log -p -2`
3. With summary of files modified: `git log --stat`
4. One line : `git log --oneline`


## Discarding changes
1. Discard all local commits to a branch to make the branch identical with remote - `git reset --hard @{u}`
2. Revert specific commits i.e. add a new commit that reverts a commmit - `git revert <commit>...`

## Git Merge/Rebase
1. Git rebase master onto a branch (assuming the branch is checked out ) - `git rebase master`
2. Pushing changes to remote branch after rebase. Since rebase changes the branch history, can't simply push changes to it. So need to force a push `git push -f`. Don't do it if it's a shared branch.

## Git References
1. `HEAD^n` refers to nth commit before HEAD
