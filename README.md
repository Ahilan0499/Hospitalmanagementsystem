# Hospital management system 
The Hospital Management System is a web-based application designed to streamline and automate various administrative and operational tasks within a hospital or healthcare facility.

## Features
- **Patient details
- **Appointments
- **Doctor details
- **Hospital details

## Technologies Used
- Backend Framework: Django
- Database:MYSQL Workbench
- API: Django REST Framework
- Version Control: Git

## setup
- create folder in your directory like Hospitalmanagement
- Create a .env file in the project root
  python -m venv hospitalenv
- activate the virtual environment
  hospitalenv\scripts\activate
- install djangoframework
  python -m pip install django
- next to create project
  python -m django startproject hospitalmanagement
- To create application using commend
  python manage.py startapp hospitalapi
- To run the application
  pyhton manage.py runserver
- To create file and add column in database using the commands are
  python manage.py makemigrations
  pyhton manage.py migrate
  
## Result
Response methods:
    Operation       	HTTP/HTTPS Methods	          Description
      Read	               get 	                Reading/getting data
      Create	             Post	               Creating/posting /inserting data
      Update	             Put                     Put-complete update
      Delete	            Delete	                 Deleting data



