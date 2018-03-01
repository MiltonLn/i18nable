# How to translate a web site using Django

![Descriptive image](talk.jpg)

This is the repository for the live demo shown at my Python Cali meetup talk

Here you can dig into the code and learn how to translate a project with Django

In the `master` branch is the code of the example with the translations implemented.
If you want to do it yourself, you can checkout to `base` branch and do the
steps described in my [blog post about this topic](http://www.lalogiadepython.com/2018/03/01/c%C3%B3mo-traducir-un-sitio-web-con-django/).

## Installation

* Clone the project `git clone https://github.com/MiltonLn/i18nable`
* Create a virtualenv
* Install the requirements `pip install -r requirements.txt`
* Migrate `python manage.py migrate`
* Run the server `python manage.py runserver`