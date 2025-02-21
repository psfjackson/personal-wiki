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




