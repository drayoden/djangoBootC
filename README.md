django bootcamp tut from CodingEnterpreneurs 10/05/20 -- brushup on django stuff
---
For this tut, project=bootc, app=products, app=profiles
---
* `pip install django==3.1.2`
* `django-admin` -- list of commands
* start an app (use one)
  * `django-admin startapp <name> .` -- note ending period (current folder)
  * `python mananage.py startapp <name>` -- no ending period
* app.models - create db schema
* project.settings.py - register apps in  INSTALLED_APPS
* `manage.py makemigrations` -- creates empty db and scripts that will be applied with 'migrate' command (next)
* `manage.py migrate` -- updates/writes/applies changes to db using scripts created above and on first run creates default tables for admin console, etc.
* NOTE: to reinitialize the db if everything goes south:
  * for each app delete everything inside app.migrations (except for __init__.py) 
  * delete db.sqlite3 or online db
  * debug problem and rerun `makemigrations` and `migrate` commands
* register models with the admin console by updating the app.admin.py file: `admin.site.register(App)` -- miminum required
* create a superuser to login to the admin console: `manage.py createsuperuser`
* run dev server: `manaage.py runserver`
* using the shell:
  * `manage.py shell` -- starts the django shell... `exit()` to close shell
  * `from app.models import <model class>`
  * `<model class>.objects.create(<property>=data,[],[],...)` -- data could be text '', number, object, etc. -- inserts data into db.
  * `<model class>.objects.get(id=#)` -- get pointer/handle to object from db
  * `obj = <model class>.objects.get(id=#)` -- assign poiner/handle to object
  * `obj.<property=data,[],[],...>` -- update this property in object
  * `obj.save()` -- duh
  * `obj.delete()` -- duh











