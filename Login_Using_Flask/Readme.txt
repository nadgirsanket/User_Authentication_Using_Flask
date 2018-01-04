A basic website has been built using Python and Flask to do the following:
1.	Simulate a user login
2.	Redirect the user to a welcome/landing page
This is a simple website that has a login page, welcome page and index page that shows up only after successful user authentication. Architecture of this project is simple and standard which makes use of flask-WTF forms, models, configuration file and SQLAlchemy for the database. The secret_key needed for session has been generated using os.urandom(24) command and stored in secret_key.txt file. Bcrypt is used for password hashing to secure password from being exposed as plain text. wtforms.validators is used to validate data required and field lengths. The landing page displays the users present in the system along with their details.

Required packages for the program to run:
bcrypt==3.1.4
cffi==1.11.2
click==6.7
Flask==0.12.2
Flask-Bcrypt==0.7.1
Flask-SQLAlchemy==2.3.2
Flask-WTF==0.14.2
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
pbr==3.1.1
pycparser==2.18
six==1.11.0
SQLAlchemy==1.1.15
stevedore==1.28.0
virtualenv==15.1.0
virtualenv-clone==0.2.6
virtualenvwrapper==4.8.2
Werkzeug==0.13
WTForms==2.1


To run the program:
On Windows machine:
1. Create a virtual environment in “….\Login_Using_Flask” directory using “virtualenv –no-site-packages venv”
2. Activate the virtual environment by traversing to ..\Login_Using_Flask\venv\Scripts and running "activate"
3. Locate the file in the directory ..\Login_Using_Flask\app\Login.py
(make sure all the required packages are installed)
4. Run the file using command (without quotes): "python Login.py"
5. Open the localhost:5000 on browser for login page
6. Login using one of the 3 users in the database with below details:
	a. Username: admin, password: admin1234
	b. Username: Alice, password: alicepasswd
	c. Username: Bob, password: bobpasswd

On Linux machine:
1. Create a virtual environment in “…./Login_Using_Flask” directory using “virtualenv –no-site-packages venv”
2. Activate the virtual environment by traversing to “..../Login_Using_Flask” and running "source venv/bin/activate"
3. Locate the file in the directory “….../Login_Using_Flask/app/Login.py
4. Run the file using command(without quotes): "python Login.py"
5. Open the localhost:5000 on browser for login page
6. Login using one of the 3 users in the database with below details:
	a. Username: admin, password: admin1234
	b. Username: Alice, password: alicepasswd
	c. Username: Bob, password: bobpasswd

Required packages installation:
1.	Install virtual environment using “pip_install virtualenv”
2.	Install flask using “pip install flask”
3.	Install flask_bcrypt using “pip install flask_bcrypt”
4.	Install SQLAlchemy using “pip install SQLAlchemy”
5.	Install flask-WTF using “pip install flask-wtf”
