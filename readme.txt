Follow next steps to run this app sucessfully:

1.Clone repository in your pc, using command: "git clone [repository url]"

2.Create a virtualenv and install all requirements, using command "pip install -r [path to requirements.txt]" (you should activate environment before)

3.Create file SETTINGS_DATA.json in "MagrasBox" folder and write it down there: "{SECRET_KEY: [your secret key], "db_password: [password for your database] }"

4.You can use any database you want, but i chose postgresql, so download it the way you want, create user with any name and db with also any name.
All you have to do is to edit database data in settings.py. Everyting is quite clear there, if you know what database is and how to use it.

5.Make migrations for all apps, that have models in it. Do it, using "python manage.py makemigrations [app name]" for each. Then just "python manage.py migrate"

6.Install docker and create redis image to have chat working. Do it, using command "docker run -p 6379:6379 -d redis:5".

7.Create superuser, using command "python manage.py createsuperuser", make up a name and password for superuser profile.

8.Run the server, using python manage.py runserver.
