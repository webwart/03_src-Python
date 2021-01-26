# Why

I want to learn the sue of VS code , Python , Django , Dash Plotly.
Order of learning MS tutorial Python, MS tutorial Djangao, Django tutorial , Testing Goat tutorial.

DepOps goals:  a) work on Naples b) add syncing with github / uberspace / USB c)

## Journal

On NapPub I did create the directory.

### SAT 01-12-2018

-1-
Alt+Shift+P Select: Interpreter
            Terminal: Create New Integrated terminal. -> This opened the git-bash shell and I could execute: .> python -m pip install matlibplot (which installs also   numpy)

-2- Settings¦Workbench¦launch.json
THe settings contains parameters for all instances of VScode of the current user.WORKBENCH contains all parameters for the project. however, when I launch the code the parameters found in launch.json are prevalent.
WORKBENCH might play a role when I work on MilPub and NapPub on the same project.

### SUN 02-12-2018

I advanced in this tutorial https://code.visualstudio.com/docs/python/tutorial-django .
I start to master VScode as well. Using the debugger is teh way to go. When I start it with F5 it saves all the files. I can stop the debugger run with SHIFT+F5
>N: https://code.visualstudio.com/docs/python/tutorial-django#_create-a-superuser-and-enable-the-administrative-interface


The original django documentation is here:
https://docs.djangoproject.com/en/2.1/intro/tutorial01/

I used httpTrack to download the documentation.

file:///C:/Users/Public/Documents/PUB-Biblio/Doc-Django-Pyton/DjangoDoc/docs.djangoproject.com/en/2.1/index.html



### SUN  23-12-2018
I did start the project mysite as shown in the Django documentation. The directroy structure is different comparing the VScode with the Django tutorial. Django tutorial:
\mysite\
    db.sqlite3
    managel.py
    \mysite\settings.py
            urls.py
            wsgi.py

Select Python: Django debugger, which has the setting for the use of the python django env.
Start integrated terminal: with CTRL + SHIFT + P

VScode tutorial:

\web_project\
    settings.py
    urls.py
    wsgi.py
db.sqlite3
manage.py
\hello\
    \migrations\
    \static\
    \templates\
    admin.py
    apps.py
    forms.py
    models.py
    tests.py
    ulr.py
    views.py


I can work on the Django tutorial in the set-up shown above. 
file:///C:/Users/Public/Documents/PUB-Biblio/Doc-Django-Pyton/DjangoDoc/docs.djangoproject.com/en/2.1/intro/tutorial02/index.html

### THU  03-01-2019
I can start the application with this SP:
CHANGE:  to \mysite\
TYPE:   python manage.py runserver
OPEN:   bowser http://127.0.0.1:8000/polls/
>N: 
https://docs.djangoproject.com/en/2.1/intro/tutorial02/

### FRI 04-01-2019
BROWSER OPEN https://docs.djangoproject.com/en/2.1/intro/tutorial02/
SCROLL TO   Creating an admin user¶
            First we’ll need to create a user who can login to the admin site. Run the following command:
admin <> Nervi56-Ad


### SAT 05-01-2019
I learned that the admin superuser has immediately access to the data models created. The interface creates automatically web pages to add questions and choises. In addition I have the appy to automatically upload data on the command line.

TYPE in the (env) bash shell in mysite. python manage.py runserver. This will keep the servr running and each time I save a file and I reload or load a new page. the changes are immediately visible. This speeds up things a lot !

I use render when I want to use a template. I use httpreponse, when I send text only.

https://docs.djangoproject.com/en/2.1/intro/tutorial03/#raising-a-404-error

### MON 07-01-2019 
I learned django.shortcuts provides the method render() and let_get_404errror(), which replaces try: catch:. These shortcuts are usefull, but hide a bit what is going on.
https://docs.djangoproject.com/en/2.1/intro/tutorial03/#removing-hardcoded-urls-in-templates

### WED 09-01-2019
I did not master the previous section, where the HTML forms are introduced. I need to redo it. However I will first finish the section below, since this might correct the errors I made before. (see 10-01-2019)
https://docs.djangoproject.com/en/2.1/intro/tutorial04/#use-generic-views-less-code-is-better

### THU 10-01-2019
07:45 I did correct the errors from yesterday. I forgot to save files and had the imports wrong. I did read ahead athe section about generic views. I will try it later today. I plan to keep the files with the non-generic-views and create new files for the generic-view code.

https://docs.djangoproject.com/en/2.1/intro/tutorial04/#use-generic-views-less-code-is-better

### FRI 11-10-2019
I could do the changes for the generic view quiete easily, but my understanding of it is not very clear. 
https://docs.djangoproject.com/en/2.1/intro/tutorial05/#writing-your-first-django-app-part-5

### SAT 12-10-2019
I can start the environement within VScode within a bash terminal. use
source c:/Users/Public/src/djangoVSC_MMdoc/env/Scripts/activate
once I am done I can close the env with deactivate.

I learned how to add test to the application. I need to remember that adding test_ before a method name I create a test if I import from django.test import TestCase and create a class MyTests(TestCase)


https://developer.mozilla.org/en-US/ -> Nice Django and web technologies tutorial from Mozilla.

https://docs.djangoproject.com/en/2.1/intro/tutorial05/#test-a-view

### SUN 13-01-2019
I forgot almost the log-in for localhost/admin/  Here it is:  admin <> Nervi56-Ad

I made could use the shell and run the tests as shown in the tutorial. However, when I changed the code in tests.py I could not successfully run the program.
>N: correct the changes I made before
https://docs.djangoproject.com/en/2.1/intro/tutorial05/#testing-the-detailview

### MON 14-01-2019
Could not resolve the problem.

### TUE 15-01-2019
Could not resolve the problem

### WED 16-01-2019
I could run the application. The indention in polls/veiws.py class IndexView def get_queryset(self) was wrong.
 However, I still have to tests, which fail. 
>N: Try to use the debugger of VScode. Why are two tests failing ? Is this okay ?
https://docs.djangoproject.com/en/2.1/intro/tutorial05/#testing-the-detailview

### SUN 20-01-2019
Only the test with future questions fail. I still have in the test.py in def create_question the object Question underlined in VScode.
I could easily go throught the chapter with the static files. However, I selected the images such that I can hardly see the list of questions. Here it needs more estathics.
>N: https://docs.djangoproject.com/en/2.1/intro/tutorial07/

### TUE  22-01-2019

In the admin.py file I can also change the appearance of the fields. It feels like I can this should be in the view.py file. However, I will accept that the admin.py file I can use to format appearance of the page. 
>N: https://docs.djangoproject.com/en/2.1/intro/tutorial07/#adding-related-objects

### FRI  25-01-2019
I did finish the django tutorial. Now I am working on the advanced topics. I will learn how to package a django application. I do have pip and setuptools installed, which are prerequisits for the following tutorial.


>N:
https://docs.djangoproject.com/en/2.1/intro/reusable-apps/#packaging-your-app

source c:/Users/Public/src/djangoVSC_MMdoc/env/Scripts/activate

### TUE 05-02-2019
I plan to transfer the poll application on an uberspace account. I can build on this tutorial.
https://lab.uberspace.de/guide_django.html


### MON 19-02-2019
I decided to install java 11 and Mavaon on Naples. Accordingly, I added all VScode extensions offered for Java Development. I can use java and spring to learn how to publish on Azure. However, at this stage I need to understand the following results.

$ java -version
java version "1.8.0_201"
Java(TM) SE Runtime Environment (build 1.8.0_201-b09)
Java HotSpot(TM) 64-Bit Server VM (build 25.201-b09, mixed mode)

$ javac -version
javac 1.8.0_152

$ mvn -version
Apache Maven 3.6.0 (97c98ec64a1fdfee7767ce5ffb20918da4f719f3; 2018-10-24T20:41:47+02:00)
Maven home: C:\Program Files\apache-maven-3.6.0
Java version: 11.0.2, vendor: Oracle Corporation, runtime: C:\Program Files\Java\jdk-11.0.2
Default locale: de_CH, platform encoding: Cp1252
OS name: "windows 10", version: "10.0", arch: "amd64", family: "windows"

### WED 20-02-2019
-1- Python¦Uberspace¦Django
To activate the environment for python and Django, I 
.> cd Django/env/bin/
.> chmod +x ./activate
.> cd ~/Django
.> source ./env/bin/activate
(env).> pip install --upgrade pip
(env).> deactivate
.> ls

>N: I need to decide between the two ways of setting up django. Look at the goat.
VScode Django set-up:   web-project and hello-app are on the same level
Django docs set-up: mysite (project) and polls-app are on different levels

ENTER:  hyb <> t uttle ; rak <> o lbers ; web <> w olf

### SAT  23-02-2019

Set-up of Django did not work. Might the 
https://lab.uberspace.de/guide_django.html

curl -I localhost:62252

When I used the description provided by uperlabs. Thinks worked out.


### SAT 09-03-2019

-1- DevOps¦
I numbered my files for development.

-2-
In usgw\MyDjangoProject.ini I changed to
http = 0.0.0.0:62252

### SAT 14-04-2019
In the future I might switch from src to jnb director. I need to learn if I need to open a folder or workbench.