

superuser <>  N56 Te  rainer.warth@hotmail.ch

## Journal

###  SUN 27-12-2020

-1- I created the list page. Until now it seems a normal Django app.
>N: https://realpython.com/django-view-authorization/  --OKAY--

-2- I can use a .json file to load data into the Django database. This is usefull when I get data from a different aplication. The format of the .json file I get from a dumpdata.

```
# Command to get data out of the database
.> python manage.py dumpdata core.blog --indent 4  --output 1748_coreBlog.json  --verbosity 3
# Command to load data into the database.
.> python manage.py loaddata 1748_coreBlog.json

```

-3-Django uses sessions to manage the state of a user. Sessions are managed through middleware. You can read more about these concepts in the Django documentation on sessions and middleware.
>N: https://realpython.com/django-view-authorization/#implementing-django-view-authorization  --OKAY--

-4- Finished this part as well.