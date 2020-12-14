# Overview

Corey Schäfer has nic video on how to use VScode for python development. The length of the video is 01:15:16.

https://www.youtube.com/watch?v=-nh9rCzPJ20

Colt Steele has a nice video on good extension for VScode and a list of good Shortcuts.
https://www.youtube.com/watch?v=rH1RTwaAeGc&t=555s
Live Server

## Joural

### FRI  02-08-2019

Created the directory and watched video.
>Learn: I can change the python interpreter on clicking the current python interpreter line in the left bottom corner. When I open VScode and I create new python file, it will use the last python interpreter, even it was a virtual env. However, VScode, does not virtuel env, only interperters,which are in the path.

12:00

### SAT 03-08-2019

12:00: about .vscode/settings.json file
There are default settings and user settings. Both are .json files. To adapt the settings to my interests, I have to copy from defaul settings to user settings.
CTRL + SHIFT + P

00:25:  Virtual environement in directory

Use CLI: .> python -m venv <Name of virt env. usually env>
The extension -m means that the module venv shall be run.

VScode adds this line to .vscode\\settings.json (user settings !) automatically, when I switz to the venv by selecting in the left lower corner.
{
    "python.pythonPath": "venv\\Scripts\\python.exe"
}

If I want to use a Virtual environment somewhere else on the machine.I have to add the full path to the settings.json file in order to use a different virtual environment. If I open the terminal VScode starts automatically the select virtual environment.

raine_sq8qzvo@Naples MINGW64 /c/Users/Public/03_src/python/coreySchäferVideo
$ source c:/Users/Public/03_src/python/coreySchäferVideo/venv/Scripts/activate
(venv)
raine_sq8qzvo@Naples MINGW64 /c/Users/Public/03_src/python/coreySchäferVideo
$ ls
00_coreyschäfervideo.md  script.py  venv
(venv)

If I use pip now, the new module will be installed in venv.
I did the requests example. On the command line it works fine, but VS.code does not show the  Intelligence for the imported requests module.

00:32   Install Autoformatter

ALT + SHIFT + F automatically formats the document, but only if a formatter is installed. When no formatter is installed, VScode does propose one.

CTRL + SHIFT + P than type sort imports. VScode proposes Refactor Imports

00:40:  Run python code

Installed .run plug-in. Now I have run buttom on top right corner. By default .run usess the python from th system, however I can change this.

00:46:    Provide input.
If I run the python script with .run. I cannot do input. I need to use VScode > RIGHT CLICK > Run File
I added code-runner settings to .vscode/settings.json

    "code-runner.clearPreviousOutput": true,
    "code-runner.showExecutionMessage": false,
    "code-runner.executorMap": {
        "javascript": "node",
        "java": "cd $dir && javac $fileName && java $fileNameWithoutExt",
        "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "cpp": "cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "objective-c": "cd $dir && gcc -framework Cocoa $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "php": "php",
//        "python": "python -u",
        "python": "$pythonPath -u $fullFileName"
        "perl": "perl",
        "perl6": "perl6",
        "ruby": "ruby",
        "go": "go run"
        }

>N:  00:47:   Git Integration

00:59:  Debugging

01:03:  Unit Testing

01:10: More editor set-up

TUE 15-08-19

Corey has video about pip and virtual environments. However, the page https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ gives a very good summary.

A useful command is:

..> pip list --outdated
Package                  Version   Latest    Type
------------------------ --------- --------- -----
alabaster                0.7.10    0.7.12    wheel
astroid                  1.6.5     2.2.5     wheel
Babel                    2.5.3     2.7.0     wheel
certifi                  2017.11.5 2019.6.16 wheel
colorama                 0.3.9     0.4.1     wheel
docutils                 0.14      0.15.2    wheel
idna                     2.6       2.8       wheel
imagesize                0.7.1     1.1.0     wheel

## SAT  07-09-2019

Corey has nice video about  __main__ and __name__  
I will practice its use. Look at ANKI entry and  ckeck if I have somewhere else already some .py files
