# Python working environmet and code samples

This is the top-directory of my python code learning area. The first 4 month of 2020 I want to progress to the next level of python programming and machine learning.

## Goals

1. Define a working environment, where I can use python code on Win10 and uberspace.
2. Experiment with Djangon and Flask framework
3. Experiment with Machine Learning, algrorithm, and data structures
4. Experiment with python modules

## Set-up

- Naples-Desk has conda env py3p8
- python system-wide uses python 3.8., -> currently not available
- python user Sion-Desk/RAI has access to my favorite Conda-VScode-Numpy-AI-Django-Sphinx ***env_numAiDjango** environment. See Reference 1. details.
- use Git with [remote repository](https://github.com/webwart/03_src-Python) , keepass r.w at hm.ch - N56 - Gi
- I FSY  between Sion-Desk and A500GbSaT3, but not with Naples-Lab
- I down- and upload with git pull/push between SioRai and NapRai user. Accordingly NapRai git-user is NapRai at  r.w@hot.ch
.> git config --global user.name "NapRai"
.> git config --global user.email "rainer.warth@hotmail.ch"
When I push to gitlab I need to give credentials: r.w@hot.ch 56-Gi

- SQL databases

To work with data in the SQL databases I need SQL clients:

- SQLite database is ideal for local development. To see the data I use SQLiteDatabaseBrowserPortable
- MySQL is use with Wordpress. To see the data I use SQLuirrel
- MS SQL Server is use for .NET core development. To see the data I use MS SQL studio.
- In VScode I can try to use SQLtools.

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

>SP: python environment

``` text
use conda from CLI
conda update --all # updates all packages in the current environment
conda update       # updates the conda 
```

## Referennce

1. PUB\Public\04_dev\01_DevOps contains the set-up information for my Conda VScode Numpy Django Sphinx environment.
2. [Data Structures & Algrorithm](https://www.youtube.com/watch?v=bum_19loj9A&list=PLBZBJbE_rGRV8D7XZ08LK6z-4zPoWzu5H) -> Data Structures and Algorithms - teaches classes , linked lists
3. [Conda Documentation](https://docs.conda.io/en/latest/)
4. Conda Cheetsheet C:/Users/raine/Downloads/conda-cheatsheet.pdf

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

### FRI  28-02-2020

-1-  Clean-out
Moved files from python-NoGit to python. Removed directories and files, which were no more relevant.

-2-  Reevalution¦new Header
I added my new header for code files.
I go throught the files update them and evaluate how to organize them in the future.
>N: ExbXmlToCSV.py --OKAY--

### MON  02-03-2020

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

### MON 09-03-2020

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

Ref.: [git-scm](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)

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

### MON 15-06-2020

-1- Excel¦SQL¦Python
I found these two interesting references.
[How to use Excel, SQL, Python](https://www.youtube.com/watch?v=71zkSuzkJrw)

[EXcel VLOOKUP and python pandas](https://www.youtube.com/watch?v=cRELNmDpaks)

-2- Documentation

- Latex for printing books
- Markdown for readme.txt

RST and asciidoctor(FX) and pandoc remain to be compared.

### FRI 31-07-2020

-1- I want to use the datetime module to add timestamps to file content und filenames. In dateAge.py I have now a good example of how to get year, hour, day from a datetime object.

>N-OKAY: Create function which makes filenames with timestemps. use in dictionaryJobUrl -OKAY-

### SA 01-08-2020

-1- I finished the function fn_timestemp in dateAge.py, which I renamed to datime.py.

-2- Tested the function dictionaryJobUrl.py. This programm basically helps me to read a .rst file and test all records for consistency.
>N: test for number of filds, then test for order of fields. Create a set to find all variations.

### SUN 02-08-2020

-1- Corrected n-200607_JobLinks.rst

-2- Found a nice way to compare see the parsing results in notepad+ using the RIGHT KLICk > "in zweite Ansicht verschieben"

-2- In dictionaryJobUrl.py I have managed to have a list with dictionaries. Each dictionary represents a record.
>N-OKAY: Print the list nicely in to .json file -OKAY-

[linkToJson](https://moonbooks.org/Articles/How-to-save-a-dictionary-in-a-json-file-with-python-/)

### SUN 03-08-2020

-1 I can obtain nice .json files with a list of dictionaries. See: dictionaryJobUrl.py

### THU 06-08-2020

I found a reference explaining the use of .json file with a list of objects, which are transfered into an sql database. sql.py. I implemented the code an it runs fine. I used SQLlite admin to look into the database myDB.sqlite

### SAT 08-08-2020

-1- Naples-Lab\VScode - Installed the SQL Tools, which requires the node.js driver for databases connection. Therefore, I also installed node.js and selected which alles the complilation of C++ files. This resulted in almost 3 GB of software instaleld includine/updateing python and VisualSudio C binaries.

Unfortuanally, after all this I could only conect to the SQLite database file, but not see the table in it !

-2- dictionaryCompare.py - In this file I will test how to compare dictionaries.

### SAT 19-08-2020

-1- SQL Tools - I still have the problem not seeing the tables in SQL View

### SAT 25-08-2020

-1- SQL Tools in VScode

On Naples-Lab and Sion-Desk I have now installed node.js and I used npm to instal sqlite3. This installes sqlite3@5.0.0 install C:\Users\raine\node_modules\sqlite3 . However, SQL tools asks for SQLite driver (sqlite@v4.0.6) . Might this be the probelem ?

-2- SQLiteDatabaseBrowser ¦ SQuirreL SQL

Sion-Desk - I will install both software. Both might also be availabe as protable version.

### SAT 21-11-2020

Created directroy for excises from the book Programming Python from Mark Lutz (Calibre). I learned today how to use the interactive window and jupyther notbook in VScode.

C:\Users\Public\03_src\python\Topics\Book-ProgrammingPython

### Tue 24-11-2020

-1- Another eMail read article: [eMail Read](https://murhabazi.com/read-emails-python/)
-2- Refactored the names of files and directories in 03_src/python.

### THU 26-11-2020

-1- How to use [PyQt HEISE](https://www.heise.de/ratgeber/Programmieren-mit-Python-Bedienoberflaeche-via-PyQt-erstellen-4949489.html)  . Downloaded article .pdf and .docx.
PyQt is open source.  Es gibt noch PySide was von der Qt Company unterstützt wird. Es gibt noch GTK, aber es wird nicht von allen Sprachen unterstüzts. Eclipese benute SWT, was ein angepasstes Swing ist, Swing sollte aber JavaFX ersetzt werden. Kivy is a GUI framework for python for touch devices. [Kivy](https://dev.to/amigosmaker/pyqt-vs-kivy-german-5483) And then is python and electron combinatoin see: [python electron](https://www.ahmedbouchefra.com/connect-python-3-electron-nodejs-build-desktop-apps/)

-2- Bodo Schoenfeld Blog offers good help for python MS-Access, Qt, and reading data and more. [MS-Access and python](https://bodo-schoenfeld.de/python/)

### THU 27-11-2020

-1- Refactoring and documention of template.py. I started adding type hints. I found links to python documentation advices on realpython.  
>N: Get a set-up to learn the use of docstrings with python.

### SAT 05-12-2020

-1- I did change/create the files fileDir_Get and filedDir_Set. I use pathlib to create files and directories and get a list of file tree.

### SAT 20-12-2020

-1- Progressed nicely with realpython django tutorial: awesome-website and _personal_portfolio.

### SUN 27-12-2020

-1- I finished _awesome-website. Here I have the links to the 3 Part Django tutorial. I would use it to translate into German and understand in Detail how it works.

[Get started Django, realpython](https://realpython.com/get-started-with-django-1/)
[User management Django, realpython](https://realpython.com/django-user-management/)
[View authorization, realpython](https://realpython.com/django-view-authorization/)

I am using Django 3.1.xx ,which is different to 3.0 in the use of pathlib. Details I find [here](https://docs.djangoproject.com/en/3.1/releases/3.1/)

### TUE 29-12-2020

-1- I further improved my Django set-up. TDD Django from Harry Percival. Furthermore, I installed Geckodriver in and selenium in the env_DjBs environment.

>N: [Obey the testing goat](https://www.obeythetestinggoat.com/)

### TUE 07-05-2020

-1- Created new conda environment with python 3.8.8 named py3p8
>N: Add Sphinx, Django, numpy etc. to env py3p8

### TUE 07-05-2020

-1- Installed python 3.10 on Naples-Lap. I can use python for 3.9 and py for 3.10 and created newFeaturesPy3p10.py and newFeaturesPy3p9.py

### TUE 09-11-2021

-1- Documentation ¦ I am cleaning out old pyhton Video class from Eric Camlin. I can probably find them on EDX. I  used the classes in 2018.
[Robust Python, Eric Camplin,edx](https://coursesplanet.com/courses/introduction-to-python-creating-scalable-robust-interactive-code)

### TUE 09-11-2021

-1- April moved for luxury fashion to Python coding.
[https://www.vogueandcode.com/](https://www.vogueandcode.com/about)
[Setting up VS Code for Python Beginners](https://www.youtube.com/watch?v=7FltByLPnrg)
[ZoomIt, nice tool for demos](https://docs.microsoft.com/en-us/sysinternals/downloads/zoomit)

### TUE 06-07-2022

-1- I prepare my set-up for youtube recordings. Have fun
