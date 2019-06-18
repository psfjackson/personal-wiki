# Git Commands

##Git Commands in terminal

Useful git commands. This is to be used as a memory promtp. 

## Pushing local files to new repo

```git 
git init

git add .
git commit -m "comment"

git remote add origin remote repository URL
git remote -v

git push origin master

## Creating .gitignore locally
```

## Updating git url

```git 
$ git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
```


## Creating .gitignore locally

```git
cd ./~ (in to working directory)

touch gitignore.txt
code . //add rules and save
mv gitignore.txt .gitignore
```

## Remove git tracking from project

inside ./dir

```git
rm -rf .git
```



