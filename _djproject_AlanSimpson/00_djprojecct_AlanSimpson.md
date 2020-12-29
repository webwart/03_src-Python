# Alan Simpson tutorial on Udemy

## set-up
I do run the commands on Sion-Des and Naples-Lab. db.sqlite3 is not saved by Github. 

Naples-Lab:  django superuser amin_Nap <> Ner56 Dj r.w@hot.ch
Sion-Des:  django superuser amin_SionDes <> Ner56 Dj r.w@gmail
.ch
OneDrive-Rai: django superuser amin_OneDrive <> Ner56 Dj  r.w@hot.ch


http://127.0.0.1:8000/admin


I use the env_numAiDjango. On Sion-Des this is a  Django 3.0 version.

Auflistung der Ordnerpfade
Volumeseriennummer : C20B-F222
C:.
└───_djproject   # Webseite / Projectname
    └──
    
Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       17.04.2020     21:05                _djproject      #  here we have the url.py file which is looked up by the web-server
-a----       17.04.2020     21:16            127 00_djprojecct.md
-a----       17.04.2020     21:14         131072 db.sqlite3
-a----       17.04.2020     20:59            651 manage.py

django-admin startproject _djproject
cd .\_djproject\
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

### 05-Video-AS_Apps

1. An App is  portable unit of functionality. Name it withlower-case characters no special characters. The name should be plural (posts) of the Apps main model (Post).
2. Allways two steps to adding an App: a) python manage.py startapp <appname> b) Add app name to INSTALLED_APPS in settings.py.
3. Create allpages in which I will have css , images , javascript , basehtml
4. TYPE: python manage.py startapp allpages , then add to _djprojecct/settings.py
5. TEST:  python manage.py runserver  
''' python
INSTALLED_APPS = [
    'allpages.apps.AllpagesConfig'
'''
### 06-Video-AS_Apps
Created the following folder structure:  
(env_numAiDjango) PS C:\Users\Public\03_src\python\_djproject> tree allpages
Auflistung der Ordnerpfade
Volumeseriennummer : C20B-F222
C:\USERS\PUBLIC\03_SRC\PYTHON\_DJPROJECT\ALLPAGES
├───migrations
│   └───__pycache__
├───static
│   └───allpages
│       ├───css
│       ├───images
│       └───javascript
└───__pycache__

### 07-Video-AS_Aptps
created stylesheet.css file

### 08-Video-AS_Apps
Google fonds

Headings: Montserrat
Body Text: Source Sans Pro
Code Samples: Source Code Pro

### 09 Define your Site-Wide Picture and Colors
Used paint.net to prepare pictures.
Used the color.adobe.com wheel to select a color combination with Hex codes.
Sion-Des:\djproject\allpages\static\allpages\css\stylesheet.css
Sion-Des:\djproject\allpages\static\allpages\images\djangopony.png

>N: Update oneDrive

### 10 A Master Template

Created HTML file in _djprojct/allpages/templates/allpages/base.html

### 11 Add Header, Footer, Navigation

``` html
<body>
    <Header>Haeder</Header>
    <nav>Nav
    </nav>
    <main>
    </main>
    <footer>Footer</footer>
</body>
``` 

### 12 add Front Awesome and Bootstrap CDN link
Into the header of base.html I added the links

### 13 Django Template Language
Used in .html files. Executed on the server
{% executable code %}
{{ varuables }}
{#  comments #}

added code to base.html to find the _djproject/static in which link to /allpages/css/stylesheet.css

### 14 Make your home pages

Used {% extends base.html %} to make .html pages

### 15 Logo and Socia Media 

In need to use {% static .....} to link to the static/image or static/css folder. I added a logo, the stylesheet, and Social media link
### 16 Create my first view

1. client request -> urls.py -> views.py (gathers the data to fill into the template)-> template.html 
2. Each view is a function or a closs. Here we use functions. If there is no content: def home_view(request): return render(request, 'path/t0/xxx.html)

### 17 url.py
1. The first urls.py always seen by the request is in the project folder  -djproject/_djproject/urls.py
2. add this line to the URL patter list: path('about/', views.about_view, name='allpages-about'),

### 18. stylesheet.css
1. Added css code for header, footer, and nav bar.
2. >!!: The body { backbround-color: yellow } did not work !!

### 19. background stylesheet.css
1. Reference to a website where  I can generated a gradien of color and obtain the CSS code
2. >!!: I could not change backbround color, gradien, or add the background picture. !!

### 20. Internal links

## References


/03_src/python/Django-AlanSimpson
............../_djproject
[VideoTutorial](https://www.udemy.com/course/hands-on-django-2/) -> Alan Simpson's video tutorial on Udemy
[SuperUser](https://djangowaves.com/tag/tips-tricks/)  ->  Has an article about superuser


##  Journal

### SUN  19-04-2020
-1- set-Up¦Naples-Lab¦OneDrive-Rai¦Sion-Des
I have starte with Allan simpson on Sion-Des . With git I get all the files on Naples-Lab, but not db.sqlite3 which is ignored by gitignor.
I also started a set-up Onedrive.
>N: Check if I have on Naples-Desk also Django 3.0. ? Find out how to deal with it since the tutoriala and überspace uses Django 2.0.

### FRI  01-05-2020
Until now I learned how to use html templates and link them together. Now I will learn how to 

### WED  06-05-2020
Added Python Django to the launch file.
>N: 18 Make things pretty

### MON  01-06-2020
-1- Naples
I did clone from git /python/. Creted in anaconda the env_NumAiDjBs environment. In VScode I did run: manage.py migrate , manage.py runserver. Then I created the superuser.

``` text
.> manage.py migrate
.> manage.py runserver
.> manage.py createsuperuser --username=amin_Nap --email=rainer.warth@hotmail.ch
```

-2- Naples
I advanced with Alan Simpson UDemy Django class
>N: 20 Intenal Links

-3- Naples
Created Desktop icon which open conda ps shell  in /03_src/python/ and activate env_NumAiDjBs. For SP see
python.md.

### MON  28-12-2020
-1- I refactored files and folders. I moved the Alan Simpson final version of the project to. 
\Public\03_src\python\_djproject_AlanSimpson\doc