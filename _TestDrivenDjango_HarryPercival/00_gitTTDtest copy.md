# 00_gitTTDtest

>N: Pull the directory on Naples and add file bFileOnNap.py

----------------------------------------------
Goal:
----------------------------------------------

Main goal is to advance with the TDD goat book from Harry.
Learn the use of Django and Python.

I created the /note/ directory where I have the code from TDD goat. I use there a locl git repo.
Here I want to use github repo.
- public
- user on Milano and Naples
- use branching

----------------------------------------------
Journal:
----------------------------------------------

## TUE 19.12.2017

OPEN	www.github.com  account webwart.  
CREATE	Repository webwart/gitTDDtest  
OPEN	Git bash on Milano  
TYPE	git init in \PUB\devTddMilPub\gitTTDtest  
CREATE	aFileOnMil.py  
TYPE	$ git add aFileOnMil.py

```
	$ git commit -m 'Commit 1 for aFileOnMil.py '
	$ git status
	 On branch master
	 nothing to commit, working tree clean
	$ git remote add origin https://github.com/webwart/gitTDDtest.git   # tells git where distant repo is
	$ git push -u origin master
	$ git status
	 On branch master
	 Your branch is up to date with 'origin/master'.

	 nothing to commit, working tree clean
	$ exit
```

I then added this file (00_gitTTDtest.txt) to the repo on Mil and www.github.com.
