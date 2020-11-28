django bootcamp tut from CodingEnterpreneurs 10/05/20 -- brushup on django stuff
---
For this tut, project=bootc, app=products, app=profiles, app=emails
---
  * DAY1
---
* `pip install django==3.1.2`
* `django-admin` -- list of commands
* start an app (use one)
  * `django-admin startapp <name> .` -- note ending period (current folder)
  * `python mananage.py startapp <name>` -- no ending period
* app.models.py - create db schema
* project.settings.py - register apps in  INSTALLED_APPS
* project.settings.py - remove SECRET_KEY (make an empty string)
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
  * `from <appname>.models import <model class>`
  * `<model class>.objects.create(<property>=data,[],[],...)` -- data could be text '', number, object, etc. -- inserts data into db.
  * `<model class>.objects.get(id=#)` -- get pointer/handle to object from db
  * `obj = <model class>.objects.get(id=#)` -- assign poiner/handle to object
  * `qs = <model class>.objects.all()` -- get all of the objects from the db 
  * `obj.<property=data,[],[],...>` -- update this property in object
  * `obj.save()` -- duh
  * `obj.delete()` -- duh
---
  * DAY2
---
  * create a view in `app.views.py` (function or class)
  * register the new view in `project.urls.py` -- urlpatterns[] 
  * note JsonResponse for api type of response.
---
  * DAY3
---   
  * settings.py/ROOT_URLCONF='<project name>.urls' -- sets root of project with the root urls file, kind of like var/www/index.html.
  * templates: djangobootc/templates folder -- templates/home.html -- contains the home page content
  * templates/base.html -- contains doctype, html/head/body start/end tags -- all other html files 'extend' this file.
  * app templates can be in one of two places
    * products/templates/products/detail.html -- contains specific content for products (see views.py -- product_detail_view - "products/templates/products/deatil.html -- wtf!
    * templates/products/detail.html -- I like this better, it searches here first anyway and seems more intuative
  * see 33:00 for snippet example
  * templates/products/list.html -- renders list of all products - uses for loop in template -- good for cards, porfolios, etc...
    * products/views.py -- product_list_view -- queries the db -> qs (query set) -- the context is creted useing the qs
    * urls.py -- create new path for the list of products.
  * dynamic titles -- very cool -- see 40:40













