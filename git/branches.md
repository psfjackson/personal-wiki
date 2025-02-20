
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

OR

git push origin -d 'branch name'
```

To rename a branch
```terminal
git branch 'm 'new name'
```
^ this requires for you 'push origin HEAD' and then delete the original copied branch from git hub. 

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
