# HOA

The interface is in Russian.

## Required packages

* [Python v2.6.5+](http://www.python.org)
* [Django v1.5](http://djangoproject.com)
* [django-annoying v0.7.7+](https://github.com/skorokithakis/django-annoying)
* [django-bootstrap-toolkit v2.8.0+](https://github.com/dyve/django-bootstrap-toolkit)
* [django-nested-inlines](https://github.com/Soaa-/django-nested-inlines)

## Used Javascript libraries
* [Bootstrap v2.3.1](http://twitter.github.com/bootstrap/)
* [jQuery v1.9.1](http://jquery.com/)
* [Messenger v1.2.3](http://github.hubspot.com/messenger/)
    * [Backbone.js v0.9.10](http://backbonejs.org/)
    * [Underscore.js v1.4.4](http://underscorejs.org/)
* [jQuery plugin: Validation v1.11.0](http://bassistance.de/jquery-plugins/jquery-plugin-validation/)

## Installation instructions

* Insert your database settings in settings.py
* You can modify the START_DATE variable in settings.py to your needs. It is needed if the data is imported and you start to work with the program after you already have some data. The variable has to hold the date when you started to work with the program.

* Run
```
python manage.py syncdb
python manage.py collectstatic
```
