Django backend for Real Estate - BSR The project is currently in working state, and some API's are under development To run the project follow the following steps

(Added property details such as FAQ' and User Favourite functionality)

Clone the git repo git clone

Run the following command on terminal to install all the requirement module pip install requirements.txt

Run the command python manage.py flush python manage.py makemigrations (In case this does not work, run "python manage.py migrate --run-syncdb" ) python manage.py migrate python manage.py runserver