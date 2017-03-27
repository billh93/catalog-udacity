# Project 3: Item Catalog

## What it is and does
Runs a video game based site that stores details of
video games in the 4 consoles of the game industry. The user can
login via Google or Facebook in order to add their own video games.

## Required Libraries and Dependencies
The project code requires the following software:

* Python 2.7.x
* [SQLAlchemy](http://www.sqlalchemy.org/) 0.8.4 or higher (a Python SQL toolkit)
* [Flask](http://flask.pocoo.org/) 0.10.1 or higher (a web development microframework)
* The following Python packages:
    * oauth2client
    * requests
    * httplib2


You can run the project in a Vagrant managed virtual machine (VM) which includes all the
required dependencies (see below for how to run the VM). For this you will need
[Vagrant](https://www.vagrantup.com/downloads) and
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) software installed on your
system.

## Project contents
This project consists the following files and directories:

* `project.py` - The main Python script that serves the website. If no database
    is found, one is created and populated by `db_setup.py`.
* `fb_client_secrets.json` - Client secrets for Facebook OAuth login.
* `g_client_secrets.json` - Client secrets for Google OAuth login.
* `README.md` - This read me file.
* `/static` - Directory containing CSS and Javascript for the website.
* `/templates` - Directory containing the HTML templates for the website, using
    the [Jinja 2](http://jinja.pocoo.org/docs/dev/) templating language for Python.
    See next section for more details on contents.
* `db_connect.py` - Function for connecting to the database.
* `db_setup.py` - Defines the database classes and creates an empty database.
* `/models` - Directory containing modules that are being used and the database schema.

### Templates
The `/templates` directory contains the following files, written in HTML and the Jinja2
templating language:

* `flash_msg.html` - Renders the flash message when a user adds, edits
    or deletes a video game and when user signs in or out.
* `deleteItem.html` - Delete video game confirmation page.
* `editItem.html` - Form to edit the details of a video game.
* `home.html` - The default page, which lists the 4 game consoles.
* `items.html` - A page that lists the games belonging to a single console.
* `base.html` - This defines the common layout of the website and is the parent
    for all the other template pages.
* `login.html` - A login page featuring OAuth Goolge+ and Facebook login buttons.
* `newItem.html` - A form for creating a new video game.

## How to Run the Project
Download the project zip file to you computer and unzip the file. Or clone this
repository to your desktop.

Open the text-based interface for your operating system (e.g. the terminal
window in Linux, the command prompt in Windows).

Navigate to the project directory and then enter the `vagrant` directory.

### Bringing the VM up
Bring up the VM with the following command:

```bash
vagrant up
```

The first time you run this command it will take awhile, as the VM image needs to
be downloaded.

You can then log into the VM with the following command:

```bash
vagrant ssh
```

More detailed instructions for installing the Vagrant VM can be found
[here](https://www.udacity.com/wiki/ud197/install-vagrant).

### Make sure you're in the right place
Once inside the VM, navigate to the tournament directory with this command:

```bash
cd /vagrant/catalog
```

### OAuth setup
In order to log in to the web app, you will need to get either a Google+ or Facebook
(or both) OAuth app ID and secret. For Google, go to the
[Google Developers Console](https://console.developers.google.com/) and for Facebook,
go to [Facebook Login](https://developers.facebook.com/products/login).

Once you have your credentials, put the IDs and secrets in the `fb_client_secrets.json`
file for Facebook and `g_client_secrets.json` for Google.

You will now be able to log in to the app.

### Run project.py
On the first run of `project.py` there will be no database present, so it creates
one and populates it with sample data. On the command line do:

```bash
python project.py
```

It then starts a web server that serves the application. To view the application,
go to the following address using a browser on the host system:

```
http://localhost:5000/
```

You should see the 4 video game consoles that were added to the database. Go ahead and
explore the web site. To add a game, you'll need to log in first with either a
Google or Facebook account.


### Shutting the VM down
When you are finished with the VM, press `Ctrl-D` to logout of it and shut it down
with this command:

```bash
vagrant halt
```
