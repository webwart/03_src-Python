# Documentation of classes, modules, functions

I wantto use Shinx to document and upload to Read the Docs (RTD)

https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html#

[Shinx for technical Writer](https://www.ericholscher.com/blog/2016/jul/1/sphinx-and-rtd-for-writers/)

Got example code frrom : C:\Users\raine\Downloads\spamfilter-py-master.zip\spamfilter-py-master which is part of the youtube: 
https://www.youtube.com/watch?v=b4iFyrLQQh4


## Journal

### TUE 01-12-2020

>SP:
CREATE.... directroy structure as shown
DOWNLOAD.. the spmafilter.py files from the git directory.
TYPED..... into the conf.py file to add
            import os
            import sys
            sys.path.insert(0, os.path.abspath('../..'))
           -1- extensions = ['sphinx.ext.autodoc' , 'sphinx.ext.autosummary' , 'sphinx.ext.autosectionlabel' , 'sphinx.ext.viewcode' ]
RUN....... (base) C:\Users\Public\03_src\python\Topics\ClassesDocsRTD\docs-ClassesDocsRTD>sphinx-apidoc -o . ../..

I am still confused how this all works together, but I have now a way to test a couple of things I want to understand.
>N: use mainClassesDocsRTD.py to create your own template.py with type hinting and docstrings. REmove the simplebt directories.