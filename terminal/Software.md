# Software

Software related terminal commands.

## Updates

To apply updates through terminal

```terminal
sudo apt-get update        # Fetches the list of available updates
sudo apt-get upgrade       # Strictly upgrades the current packages
sudo apt-get dist-upgrade  # Installs updates (new ones)
```

## Opening files

To open all files in VScode

```terminal
code . 
```

To open file in Chrome

```terminal
google-chrome ./filename
```

To open file in firefox

```terminal
firefox ./filename
```

## Branches

To check branch(s).

``` terminal
git branch
```

To create a new branch
``` terminal
git branch -c 'name of branch'
```

To change which branch you are on
``` terminal
git switch 'name of branch'
# can also use git checkout 'name of branch'
```

To remove or delete a branch
```terminal
git branch -d 'branch name'
```

## Merging

Mental model: To merge a branch, you pull in to the 'branch' that you want to merge updates from. For example, if you want to 
**add changes** from a **development branch** to your master branch, you should **switch to the master** and merge or 'pull in' the development branch. 

```terminal
git switch 'branch you want to merge in to'

git merge --no-ff --no-commit 'branch you want to pull from'

# adding to master:
git switch master
git merge --no-ff --no-commit development
git status

#Once we solve the conflicts, or if there is no conflict, we commit and push them
git commit -m 'merge test branch'
git push
```

## Pushing to Branch

To push comitted changes to branch (have to be on the correct branch)
```terminal
git push origin HEAD
```

## Committing

To add all files for before comitting
``` terminal
git add --a
# git all . didn't add all changes
git commit -m "useful message"
```

## File Creation

Creating a new folder
``` terminal
mkdir 'name of folder'
```

Creating a new file
```terminal
touch 'filename'.'filetype
```

## Reviewing Commit Log

```terminal
git log --oneline --graph --all
```




