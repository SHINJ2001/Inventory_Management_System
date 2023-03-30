# Inventory Management System For A Machine Shop
This inventory management system intends to maintain the inventory of any
regular machine shop that requires a database to maintain track of their current
inventory, their costs, rejections for their parts and also their customers.  

Allows privileged user like manager and normal user for working staff registered
into the company's database.

## How does it work?
The project involves the usage of MySQL, hence before using it on your computer make sure you have a MySQL server running on your computer.
Then go to the following directory 
```shell
Inventory_Management_System/Inventory_Management/settings.py
```
Here change the user and password to the one created on your personal computer. You may change the host to appropriate IP address of the host, but if you are running it on your own computer let the address be the same.  

Once you are up and running type the following commands onto your command line to apply the changes to the project(Make sure you are in the proper directory, i.e. the directory where the entire project is stored.)

```shell
python manage.py makemigrations inventory
python manage.py migrate
```

Now launch the application using 

```shell
python manage.py runserver
```

You should something like this on your screen.
```shell
December 16, 2022 - 08:38:10
Django version 4.1.2, using settings 'Inventory_Management.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Now open the link shown containing the IP address of the host machine.
The application provides a user friendly interface. Create required users and start using it like any other web application!

P.S. You might want to change the MYSQL settings in Incentory\_Management/settings.py -> DATABASES section to configure the application for the databse on your machine. Change the username, password and the name of the database which would be the name assigned by you to your database.
