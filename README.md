# Merger

## About

merger is an open-source web application that (1) organizes and consolidate all the intermediate data produced during a security assessment or penetration test, and (2) generates a report based on such data and predefined templates. 

This web application employs different objects (Systems, Ports, Web Applications, Webpages, Vulnerabilities, etc.) and links them based on their relationships. These objects are organized in a tree data structure, following a general-to-detail methodology. For example a System might have Vulnerabilities and Ports, which can have Web Applications with additional Vulnerabilities. Consequently, all the data from engagements is located in a single place, easily accessible, and organized in an systematic way.

Finally, merger tackles the problem of reporting by automatically producing a report using the information collected and predefined templates. This way, analyst, engineers, and/or researchers can focus more on security findings and less in paperwork.

## Install

***Important:** Merger has been desiged for and tested in Kali Linux 2020.2*

Install using docker:

```bash
git --depth 1 clone https://github.com/sxntixgo/merger.git
cd merger
python3 setup.py -d
docker-compose up
firefox http://0.0.0.0:8080
```

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
* Improvements to the web interface,
* Tests,
* Import from security tools (nmap, nessus, etc),
* Web API.

Please see projects to see features/bug fixes in the works.

## Bugs

Did you find a bug? Please create an [issue](https://github.com/sxntixgo/merger/issues).

## License

This project is MIT license.

## Libraries, Frameworks, and Dependencies

* [Bootstrap 4](https://getbootstrap.com)
* [Django](https://www.djangoproject.com/)
* [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
* [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field)
* [matplotlib](https://matplotlib.org/)
* [psycopg2](https://www.psycopg.org/)
* [python-docx](https://python-docx.readthedocs.io/en/latest/)
 