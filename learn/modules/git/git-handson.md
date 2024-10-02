---
title: "Git Setup Hands-on"
---

**What is Git?**

*   Git is a central repository using which we can manage our project source code
    
*   Git is also called it a version controlling system
    
*   It maintains all modifications happening to a specific file
    
*   Because of versions troubleshooting and fixing bugs are easy
    
*   If something goes wrong in current version we can rollback to previous version
    
*   Records who modified, when it is modified(time stamp) and why it is modified
    
*   Git is distributed version controlling system
    
*   Git is fast when it is compared with other version controlling tools
    
*   Multiple developers can easily collaborate and work on same project
    
*   It also works as backing up our project code
    

**Getting git server to manage our projects**

Download,Install and configure git server on our own machine Create account online with

1.  GitHub
    
2.  Bitbucket
    
3.  Git Lab
    
4.  CodeCommit(AWS)
    

Create account in github.com and signin
Creating new repository in github.com 

**What is repository in git?**

*   In git repository represents a project.
    
 
**Steps to create repository**

*   New Repository → Enter repository name → select public → select README file → Create Repository.
    
**Git terminology** :

Git is client server architecture.

**Client** : git bash and server. Git hub

**repository** : group of project files to store one single area and each project has one repository. git hub has  n.no.of repositories..

**Cloning:** remote repository (my web) to getting the local → cloning → git clone **URL** (each project has one URL) → locally

**Fork**: projects are copied from **one git hub** account to **another git hub** account. 

**Local repository**: getting the **remote** repository (My web) to our local laptop. 

**Remote repository**: git hub → our created repository (My web)

**Push:** sending **local repository** changes to **remote repository**

**pull**: sending the **remote repository** changes to the **local repository Note**: git follows → 2 types of proto calls → **https** and **SSH**.


**Git workflow**

1.  we need to clone remote repository to local
    

Git clone URL
```
git clone https://github.com/githurepo/repo.git

ls
```
2.  go to the inside local repository.
    
```
cd some_folder
```
3.  files → create / modify → working area.
    
```
touch demo_file

git status → red color → working area.
```
4.  git add . (dot means file name) / filename /
    

git status

File → green color → Indexing / staging area.

5. we are getting the files to local repository → commit
    

git commit -m (m stands for message) 'rk2020' → local repository. git log

40 digits commit ID → head → head always points to latest commit.

6. push to remote repository. 
    

git push origin master

push → sending local changes to remote repository.

origin → alias name → git hub URL master (or) Main → default branch.

```
git config --global user.name "ramakrishnaj2020"
git config --global user.email "codedalehelp@gmail.com"
```

```
git push origin master → git hub account name and git hub password → remote
```


How to undo changes in working area?

File → modify → working area git checkout filename.

How to undo the changes in index/staging area File → modify → working area

git add . / file name / * → index / staging area git reset filename

How to undo the changes the in local repository. file → modify → working area

git add. / file name / * → index / staging area. git commit -m 'b123'

git log

Git reset commit ID

{/*
**Branching strategies**

1.  Master branch → default branch
    

1.  Development branch (dev ) → every team has their own branch → which is created from master branch.
    

2.  Feature branch → every developer has their own branch → which is created from dev branch. 
 
3.  Hot fix / bug fix branch ==>> errors / bugs ===> which is created from master branch ===>> errors free ==>>> hot fix / bug fix branch will delete.
    
4.  Release branch ===>> every release has one branch with version ==>> which is created from master branch ==>> once release push to remote ==>> Release branch will delete.
    

**Branch**: To develop the code of our project.

**How to create** B**ranch in locally?**

git branch Branch_name

**How to push local Branch remote???**

git push origin Branch_name **How to delete local Branch** git branch -d Branch_name **How to delete remote Branch**

git push origin -d Branch_name **How to go to inside a Branch** git checkout Branch_name


***** merging strategies in locally ****

1.  **Fast-forward**
    

1.  **Two way or recursive merge or ort**
    
2.  **Git rebase (Dangerous)**
    


**git cherry-pick**:

It picks a commit from one branch and applies it to another branch without doing merge.

**git cherry-pick commit Id**.


**How to merge the remote side changes** ===>>> pull request.

Pull request **==>> remote side branches ==>>** git hub **==>> in between the branches ==>>** merging is nothing but pull request.

**Pull request** ==>> TL / collegues ===>> approval ==>> merge pull request ==>> conform merge. pull request ==>> **source and destination**

source (right side) and destination (left side).


**tags**: tags are used to release the application or code version or feature version. list of tags to see ==>> git tag

**how to create a tag locally** ?? git tag tag_name

**Ex**:- git tag v1.0

**how to push local tag to remote ??**

git push origin taganme Ex:- git push origin v1.0

**tags are create on the particular commit**. git tag tagname commit ID

-> tags are created from the master branch only..

**how to delete a tag locally ?**

git tag -d tagname

**How to delete remote tags**

git push origin -d tagname


**git stash** :

Harsha ==>> developer ==>> mono file ==>>> working area or index area ===>> before going to commit ==>> P1 ( priority one task ==>>> 2 hours close) .

Harsha ==>>> developer ==>>> mono file ==>>> tempararily save ==>> git statsh

After completion of the p1 task ==>> temporarily save ==>> unstash ==>> after that commit.

**git stash save** ==>> temporarily save

**git stash list** ==>> stash {0}

git stash apply stash ID stash {5} **or** git stash pop stash ID stash {5} ==>> unstash

**git commit -m 'c1'**

git push origin master.


**Merge conflicts (locally)**

Harsha ==>> developer Nihar ===>> developer

Both developers are working on the same file ===>>> pqrs ===>> same line ==>> 151 Nihar ==>> developer ==>> dev branch ==>>> merge ==>>> unable to merge.

git merge tool

pqrs ==>> will open ==>> 151 << >> ==>> brackets ==>>> remove the brackets

**Pull request conflicts (remote side)**

shaker ==>> developer Sundar ===>> developer

Both developers are working on the same file ===>>> mno ===>> same line ==>> 351

Sundar ==>> developer ==>> dev branch ==>>> pull request ==>>> unable to pull request ===>> resolve conflicts.

Merge conflicts ===>>> click this ==>>>> mno ==>>> open

mno ==>> will open ==>> 351 << >> ==>> brackets ==>>> remove the brackets.



1.  **release branch**
    
2.  **pull request**
    

1.  **tags**
    

1.  **git hub ==>> backup**
    



**git fetch** ==>> Download the changes from remote repository without merging into current directory

**or** Local Repo **or** Local Branch

**git pull** ==>> Download and Merge the changes from remote repository into current directory

== **git fetch + git merge git rebase** ==>> Rewrite the commit history by moving, combining **or** applying changes from one -------

branch to another branch, creating a linear history.

**git merge** ==>> Combining the changes from one branch into another branch, creating a new

commit, the modification from both branches

**git conflicts tool** ==>> source tree

**git squash** ==>> the process of condensing multiple commits into a single commit during git rebase, creating a clear and more readable history

**git patch** ==>> A text file containing the difference between two sets of code ,used to apply changes from one codebase to another.

**git diff** ==>

1.  Shows the **difference between** changes in working directory and the staging area or index area.
    
2.  Can also be used to compare **difference between** commits, Branches and any two arbitrary points
    

-in the git repository.

**git status** ==>>

1.  Displays the current state of the **working directory** and **staging area.**
    
2.  Shows which file has been modified, which files are staged for the next commit, and which files are
    

-untracked.

**git revert** ==>>

When the developer has pushed the code wrongly to **remote repo** then he will do git revert and change files and given as new commit id and purely remote side changes.

**.git ignore** ==>> Hiding the files or folder

**git reset** ==>> when you do the git reset it will **go back** to working directory == **git reset commit id**

To Move the ALL file or Folder staging/Indexing Area to working Area **=== Eg**:- git reset ## No way to get back the files or folders after using the git reset command

**Soft reset** ==>> I want to reset the latest commit so that the **HEAD** will point to particular **commit ID Eg**:- **git reset --soft** 69f77c9fad2f918b3f1e8e2249888aa9f883293f

Before that ==>> **git log -4**

**git reset --soft HEAD~2 #here 2 is No of commit reset**

**Hard rest** ==>> After adding the file or folder staging/Indexing Area

To remove the file or Folder staging/Indexing Area and working Area == **Eg**: - **git reset --hard**

**Mixed reset** : To Move the file or Folder staging/Indexing Area to working Area

**Eg**:- **git reset --mixed file name or folder name** */}