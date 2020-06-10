# Python working environmet and code samples

This is the top-directory of my python code learning area. The first 4 month of 2020 I want to progress to the next level of python programming and machine learning.

## Goals

1. Define a working environment, where I can use python code on Win10 and uberspace.
2. Experiment with Djangon and Flask framework
3. Experiment with Machine Learning, algrorithm, and data structures
4. Experiment with python modules

## Set-up

- python system-wide uses python 3.8. 
- python user Sion-Desk/RAI has access to my favorite Conda-VScode-Numpy-AI-Django-Sphinx ***env_numAiDjango** environment. See Reference 1. details. 
- use Git with [remote repository](https://github.com/webwart/03_src-Python) , keepass r.w at hm.ch - N56 - Gi
- I FSY  between Sion-Desk and A500GbSaT3, but not with Naples-Lab
- I down- and upload with git pull/push between SioRai and NapRai user. Accordingly NapRai git-user is NapRai at  r.w@hot.ch 
.> git config --global user.name "NapRai"
.> git config --global user.email "rainer.warth@hotmail.ch"
When I push to gitlab I need to give credentials: r.w@hot.ch 56-Gi

## Getting started

- make sure all files are updated. FSY to github. 
- open directory with VScode.
- select between env_numAiDjango , system wide , or create new environment.
- select debug environment.
- when finished FSY with github
- Sion-Desk: FSY to A500GbSaT3
- Naples-Lab: Do not FSY !

>N: Add file header to .py files. Clean out and actualization of files.
>N: Uset the pathlib.py file. Deveop a system to read, write files like text, json , xml , csv. 
>N: Walk directroies and read their content

## Structure and procedures

>SP:

## Referennce

1. PUB\Public\04_dev\01_DevOps contains the set-up information for my Conda VScode Numpy Django Sphinx environment.
2. [Data Structures & Algrorithm](https://www.youtube.com/watch?v=bum_19loj9A&list=PLBZBJbE_rGRV8D7XZ08LK6z-4zPoWzu5H) -> Data Structures and Algorithms - teaches classes , linked lists

## Journal

Restart of phyton directory

### SAT  21-02-2020

-1- Git¦
On github I created the repository 03_src-Python. Then I cloned this directory into PBU\03_src\python on Naples. I added some first files and did add them to the repository with git-bash cli.

### SUN  22-02-2020

-1-  Clean-out
\pandas\ , \SphinxTest\

### THU  27-02-2020

-1-  Sion-Desk¦Git
I created a new \python\ using the git pull on Sion-Desk.

-2-  Naples-Desk¦FSY
I removed \python\ from FSY with A500GbSaT3.

###  FRI  28-02-2020

-1-  Clean-out
Moved files from python-NoGit to python. Removed directories and files, which were no more relevant. 

-2-  Reevalution¦new Header
I added my new header for code files.
I go throught the files update them and evaluate how to organize them in the future.
>N: ExbXmlToCSV.py --OKAY--

###  MON  02-03-2020

-1- Python system wide
I added python 3.7 to Sion-Desk. I can use py launcher to switch between 3.7 and 3.8 on the command line. VScode does also recognize the 3.7.
I learned to update python with patches and add new minor versions.

-2- Reevalutaion¦new Header
Advanced further and delete some files.
>N: Pandas_Edx.py --OKAY--

### TUE  02-03-2020

-1- Reevalutaion¦new Header
Moved on
>N: pro-EndNoteJabRef.py

### THU  05-03-2020

-1- Reevalutaion¦new Header
Moved on
>N: ReadXML.py

###  MON 09-03-2020
I obteined from 
[Bundesnetzagentur](https://www.bundesnetzagentur.de/cln_1432/DE/Sachgebiete/Telekommunikation/Unternehmen_Institutionen/Nummerierung/Rufnummern/ONRufnr/ON_Einteilung_ONB/ON_ONB_ONKz_ONBGrenzen_Basepage.html?nn=316054)
die local area codes.

>N: Write programm to find legal phone numbers for Germany.

### FRI  06-03-2020

-1- Reevalutaion¦new Header
I am done with the header. The header changed. I also need to define how I want to do documentation with docstring.
Now want to consilidate all these files and use them as a basis for my python book.
>N: Learn to search over mutiple files with VScode. Learn to use docstrings in python. 

### WED  18-03-2020

Django with Alan Simpson
[LINK](https://github.com/AlanSimpsonme)

I did cond

### FRI  17-04-2020
-1- pathlib
I collected some nice links to web-sites with path-lib intros. I wnt to standardize my file/directroy operations.

[Business Python](https://pbpython.com/pathlib-intro.html)  ->  nice artcle about pathlib
[Trey Hunner](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)  ->   nice article about pathlib
[Real Python](https://realpython.com/python-pathlib/)  -> nice articl about pathlib

-2- email module
Python doc offeres some nice examples. I want to try them with uberspace

### MON  02-06-2020
-1- Naples
Created a desktop icon , which launches a Powershell, activates env_NumAiDjBs, and opend VScode in /03_src/python.

>SP: Create Desktop Icon to lounch conda, VScode and acivate env

``` text
W-START...
SELECT.... Anaconda powershell prompt
R-KLICK... >Mehr > Dateispeicheort öffnen
OPEN...... C:\Users\raine\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)
SELECT.... Anaconda powershell icon
CREATE ... Verknüpfung from Anaconda Powershel icon
MOVE ....  Verknüpfung Anaconda Powershell ICON to desktop.
R-KLICK... and select Eigenschaften
REPLACE .. in Ziel:

%windir%\System32\WindowsPowerShell\v1.0\powershell.exe 
-ExecutionPolicy ByPass
-NoExit
-Command "& 'C:\Users\raine\Anaconda3\shell\condabin\conda-hook.ps1' ;
          conda activate 'C:\Users\raine\Anaconda3' "

WITH ..... Makesure to adapt location of venv !!!

%windir%\System32\WindowsPowerShell\v1.0\powershell.exe 
-ExecutionPolicy ByPass 
-NoExit
-Command "& 'C:\Users\raine\Anaconda3\shell\condabin\conda-hook.ps1' ;
 conda activate 'C:\Users\raine\Anaconda3\envs\env_numAiDjango' ; code . "

REPLACE.. in Ausführen:

%HOMEPATH%

WITH......

C:\Users\Public\03_src\python\
```

### FRI  06-05-2020

-1- Sion
I did create desktop icon to launch conda, VScodeand activate env. See SP above, I just adjusted the env name.

### FRI  10-06-2020

-1- Sion
Change git user.name to SioRai with git config --global user.name "SioRai".

-2- GIT
I learned that Git uses a series of configuration files to determine non-default behavior that you may want. For this GIT has 3 different configuration fiels.

1. System level: /etc/gitconfig
2. User level: ~/.gitconfig (or ~/.config/git/config) 
3. Repository: .git/config

Below you see the commands to see what your currently have set.

Ref.: https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration

``` text
/// Git first looks at system configuration variables \\\

(env_NuDjBs) C:\Users\Public\03_src\python>git config --system  -l
diff.astextplain.textconv=astextplain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
http.sslbackend=openssl
http.sslcainfo=C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
core.autocrlf=true
core.fscache=true
core.symlinks=false
credential.helper=manager

(env_NuDjBs) C:\Users\Public\03_src\python>git config --global -l
user.name=SioRai
user.email=rainer.warth@gmail.com

(env_NuDjBs) C:\Users\Public\03_src\python>git config --local  -l
core.repositoryformatversion=0
core.filemode=false
core.bare=false
core.logallrefupdates=true
core.symlinks=false
core.ignorecase=true
remote.origin.url=https://github.com/webwart/03_src-Python.git
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
branch.master.remote=origin
branch.master.merge=refs/heads/master
```