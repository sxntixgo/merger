# Merger

## About

merger is an open-source web application that (1) organizes and consolidate all the intermediate data produced during a security assessment or penetration test, and (2) generates a report based on such data and predefined templates. 

This web application employs different objects (Systems, Ports, Web Applications, Webpages, Vulnerabilities, etc.) and links them based on their relationships. These objects are organized in a tree data structure, following a general-to-detail methodology. For example a System might have Vulnerabilities and Ports, which can have Web Applications with additional Vulnerabilities. Consequently, all the data from engagements is located in a single place, easily accessible, and organized in an systematic way.

Finally, merger tackles the problem of reporting by automatically producing a report using the information collected and predefined templates. This way, analyst, engineers, and/or researchers can focus more on security findings and less in paperwork.

## Install

***Important:** Merger has been desiged for and tested in Kali Linux 2020.2*

Install using docker:

```bash
git clone --depth 1 https://github.com/sxntixgo/merger.git
cd merger
python3 setup.py
docker-compose up
```

Then, open `http://0.0.0.0:8080` in your browser

For detailed installation instructions can be found at [INSTALL.md](INSTALL.md)

## Features

This is the list of current features:

* Tree data structure to organize objects: Project, Point of Contact, Systems, Vulnerabilities, Attachments, Apps, Ports, Web Applications, Web Pages,
* Object linking based on their relationships,
* Report generation based on objects and templates,
* Report Templates,
* Docker deployment.

### Future features

This is the list of features on the pipeline (not in any specific order):

* Users, groups and permissions, to allow collaboration,
* Tests,
* Import from security tools (nmap, nessus, etc),
* Web API.

Please see projects to see features/bug fixes in the works.

## Bugs

Did you find a bug? Please create an [issue](https://github.com/sxntixgo/merger/issues).

## License

This project is MIT license.

## Libraries, Frameworks, and Dependencies

* [Bootstrap 4](https://getbootstrap.com) ([License](https://getbootstrap.com/docs/4.0/about/license/))
* [Django](https://www.djangoproject.com/) ([License](https://github.com/django/django/blob/master/LICENSE))
* [django-bootstrap-breadcrumbs](https://github.com/prymitive/bootstrap-breadcrumbs/) ([License](https://github.com/prymitive/bootstrap-breadcrumbs/blob/master/LICENSE))
* [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) ([License](https://github.com/django-crispy-forms/django-crispy-forms/blob/master/LICENSE.txt))
* [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field) ([License](https://github.com/stefanfoulis/django-phonenumber-field/blob/master/LICENSE))
* [Feather](https://feathericons.com) ([License](https://github.com/feathericons/feather/blob/master/LICENSE))
* [jQuery](https://jquery.com) ([License](https://jquery.org/license/))
* [matplotlib](https://matplotlib.org/) ([License](https://matplotlib.org/users/license.html))
* [PopperJs](https://popper.js.org) ([License](https://github.com/popperjs/popper-core/blob/master/LICENSE.md))
* [psycopg2](https://www.psycopg.org/) ([License](https://github.com/psycopg/psycopg2/blob/master/LICENSE))
* [python-docx](https://python-docx.readthedocs.io/en/latest/) ([License](https://github.com/python-openxml/python-docx/blob/master/LICENSE))

 