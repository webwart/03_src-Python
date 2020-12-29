# django projet

## goal

learn user management

## Journal

>N:
https://realpython.com/django-user-management/

###  SUN  20-12-2020

-1- Created superuser admin <> N56-Te

-2- Changed password N56-Te2

-3- Created /documentation/

-4- Next I will learn how to reset a password.

>N: https://realpython.com/django-user-management/#send-password-reset-links

###  MON  21-12-2020

-1- Django has an smpt eMail dev server integrated. I cans see what eMail Django would send. I need to start the smpt dev server with:

```
python -m smtpd -n -c DebuggingServer localhost:1025
```

-2- I can now send eMail with a link to reset the password.
>N: https://realpython.com/django-user-management/#change-email-templates

For this I need to got to the login page, enter admin@hotmail.ch and check for eMail in the console. The eMail contains a link to the page where I can change the pwd. Current:
admin@hotmail.ch <<>> N56 Te


###  THU 24-12-2020

-1- Learned how to create a new user. rainer.warth@gmail <> N56-Te10
>N: https://realpython.com/django-user-management/#send-emails-to-the-outside-world


###  SAT 26-12-2020

-1- I created a sandbox account with mailgun. Via Djanog awesome-website I can now send eMailt to rainer.warth@hotmail.ch 
Grab your SMTP credentials:
SMTP hostname: smtp.mailgun.org
Port: 587 (recommended)
Username: postmaster@sandboxfbfde309885f4d468aa787b641cf577f.mailgun.org
Default password: 9bfa89205c853c16cba8a5091394467c-b6190e87-25195f6a

-2- I learned how to had password und username to my environment-variable this is a saveway to keep them safe.


-3- Log-in with github
https://realpython.com/django-user-management/#log-in-with-github

conda install -c conda-forge social-auth-app-django

set SOCIAL_AUTH_GITHUB_KEY=ca072a3f1239946ed5d5
set SOCIAL_AUTH_GITHUB_SECRET=299c6c1448a4cd332d516cce9d77b29a35ef3c5f

SOCIAL_AUTH_GITHUB_KEY = os.environ.get("SOCIAL_AUTH_GITHUB_KEY")
SOCIAL_AUTH_GITHUB_SECRET = os.environ.get("SOCIAL_AUTH_GITHUB_SECRET")

I did not get to work this section properly. After I log-in to github, I am not redirected to my django -awesome application

-4- I do not think that I will continue to work on part2, where would have to fix the github log-in and do as next step adding github to new user signup.
>N: https://realpython.com/django-user-management/#select-authentication-backend

-5- Here I have the links to the 3 Part Django tutorial. Iwould use it to translate into German and understand in Detail how it works.
https://realpython.com/get-started-with-django-1/
https://realpython.com/django-user-management/
https://realpython.com/django-view-authorization/

I am using Django 3.1.xx ,which is different to 3.0 in the use of pathlib. Details I find here.
https://docs.djangoproject.com/en/3.1/releases/3.1/