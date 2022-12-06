# LocationTrackingAppBack

"LocationTrackingAppBack" is a backend application for an application that reads location data and displays and records daily route information and photos on a map.

# DEMO

You can use it by logging in, and you can select which days to display information on the calendar screen. Once a day is selected, the schedule and map for that day will be displayed, and location information and photos can be viewed.

https://user-images.githubusercontent.com/78858054/205677181-9a764ebf-63be-4759-9582-192b5e4725f9.mov

You can learn to create APIs that work with the front end through the Django REST Framework.

# Features

You can learn how to do token-based authentication, how to handle mpoint type data using GeoDjango.

# Requirement

* asgiref 3.5.2
* Django 3.2
* django-cors-headers 3.13.0
* django-environ 0.9.0
* django-filter 22.1
* django-geojson 3.2.1
* django-rest-auth 0.9.5
* djangorestframework 3.13.1
* djangorestframework-gis 1.0
* pip 22.2.2
* psycopg2 2.9.3
* PyJWT 1.7.1
* pytz 2022.2.1
* setuptools 57.4.0
* six 1.16.0
* sqlparse 0.4.2


# Installation

Install with requirements.txt.

```bash
pip install -r requirements.txt
```

# Usage

The following commands are executed to make it work in the localsever.

```bash
python manage.py createsuperuser
python manage.py runserver
```

By creating a superuser, you can log in to the admin site and even get a Token by means of an API endpoint called auth. By including the Token in the header of the HTTP request, various APIs can be called.

The auth endpoint allows users to log in, create new accounts, log out, delete accounts, etc.
- auth/login allows you to obtain a token for login by posting the correct email address and password.
- register allows you to create a new user by POSTing the user's information.
- logout removes the user's Token and puts the user in a logout state.
- myself return user information by including the token in the header.
- update/theme allows you to update theme color settings.
- update/is_tracking allows you to update location tracking settings.
- user allows crud operations of user model.
- password/reset send a password reset email by posting the email address.
- rest-auth allows you to access to django-rest-auth.
- reset/<uidb64>/<token> change the user's password if the authentication by the password reset email is correct.

The api/location allows you to call APIs that handle location information. Specifically, 
- api/location   allows crud operations. 
- api/location/update/<int:calendar__id>   can be used to update existing data.
- api/location/month/<int:user__id>   can be used to obtain an array of location data for each month.
The api/calendar endpoint allows calling the API for handling calendar data.
- api/calendar allows crud operations.
- api/calendar/month can be used to obtain daily events.

# Note

Since everything is authenticated by Token, security issues remain.

# Author

* Shunya Nagashima
* Twitter : -
* email : syun864297531@gmail.com

# License

"LocationTrackingAppBack" is under [MIT license].

Thank you!
