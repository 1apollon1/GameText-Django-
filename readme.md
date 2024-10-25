## Meta-info

**GameText** - is a web application that provides a platform for playing text role-playing games. The interface is represented by rooms, each of which has participants with certain roles and privileges. Players are provided with a chat room, which represents the entire in-game world.

**STACK**: **`Django`**, **`django-channels`**, **`Redis`**, **`PostgreSQL`**, **`WebSockets`**

## Installation

- Clone repository, using: `git clone https://github.com/slaverchief/GameText-Django-.git`

- Create a virtualenv and install all requirements, using `pip install -r requirements.txt` (you should activate environment before)

- Set the all required environment variables:
	- **SECRET_KEY** - The secret key in setting.py file
	- **DEBUG** - The value that sets the status of the DEBUG variable(1 or 0)
	- **HOST** - The address of the host where the web app is running
	- **CHANNEL_HOST** - Address for channel layers(Redis server address)
	- **db_name** - Name of app's database
	- **db_user** - User for app's database
	- **db_password** - Password for user of app's database
	- **db_host** - IP address of the server with your database

- Set up the project for your database in settings.py. In my case PostgreSQL was chosen, you can do the way you want

- Make migrations for every app, using: `python manage.py makemigrations [app name]`

- Run `python manage.py migrate`

- Set up Redis on you hardware and write its address into ENVs for this app

- Create superuser, using `python manage.py createsuperuser`, make up a name and password for superuser profile.

- Run the server, using `python manage.py runserver`.


