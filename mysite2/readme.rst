mysite2/README.rst
=====
Soil App
=====

Simple attempt at getting a package set for github development

Quick start
-----------

1. Add "soils" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'soils',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^soils/', include('polls.urls')),

3. Run `python manage.py migrate soils` to create the soils models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a soils (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/soils/ to participate in the soils.
