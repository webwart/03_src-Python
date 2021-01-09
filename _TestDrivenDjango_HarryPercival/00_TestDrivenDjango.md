# 00_05_devTTDMiPub.md

This directory moved a around a bit. I on Milano Public , has a git , moved from 05_devTTDMilPub (deleted) to here.

>N: Update name of this file , update this file with DevOps template , create venv with system 3.7 and django
>N: EVALUATE if I set-up also a director with the flask pandoc example from CT.
>N: Check

--------------------------------------------------

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

## SUN  12-05-2019
-1- 
I renamed htis file from 00_gitTTDtest.txt to 00_05_devTddMilPub

-2-
Eventually this directory will be deleted and the content goes in the 03_src or 04_dev directory.

##  TUE  24-12-2019

### MON 28-12-2020

-1- For what ever reason I had this folder in the 05_dev. Since it is a learning project, I moved it to 03_src.

-2- The TDD django project is still at 1.11v for djnagon. I will try to go through it with the latest djangon version 3.11. Here I can see how to update a project.
https://docs.djangoproject.com/en/3.1/howto/upgrade-version/

-3-	I used django-admin _superlist . to start over again. 

-4- Downloaded geckodriver for win64 and placed it  env_NuDjBs/script folder. in same env i installed conda install selenium.

### MON 02-01-2021

-1-	Today I finished section 04. In VScode I start Django dev-server and can change html, thereafter test with test_functional, which is using selenium. I also learned that without running the Django dev-sever I can run test.py. The functional tests are interestig since I manupilate Firefox browser, which I might be able to use for job-workbench.
>N: 

### MON 05-01-2021

-1- Here another explanatinon how I can use functiona and unit test with Django server

a) Django server running:
I can start Django server and do a manuel test, then perform the functional test and the unit test.
>ANKI: Django server , manual test (any browser), functional test (firefox) ,  unit test


b) Django server stopped:
When I stop the Djnago server I can **not** run the functional test, since it is like a user operating the webbrowser (in my set-up firefox). Since the Django server is not running the web-browser cannot connect to a web-site. Consequently, the test will fail with “Message: Reached error page: …. However the unit test (test.py) will still work.
>ANKI: Django server , unit test
