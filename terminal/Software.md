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

To check our a branch
``` terminal
git checkout 'name of branch'
```

To remove or delete a branch
```terminal
git branch -d 'branch name'
```

##

To add all files for before comitting
``` terminal
git add --all
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





