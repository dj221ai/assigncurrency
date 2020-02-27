This app is an attempt to build a small currency converter app in  django-rest-framework.

For activating virtual environment type source asenv/bin/activate.

install all requirements: 
pip install -r requirements.txt


It consists the basic authentication process of django-rest-framework.
It allows to Register and Login the user.


User Registration API: http://localhost:8000/users/

It Shows the balance of the user and even allow to update the balance

API for showing user balance list: http://localhost:8000/api/

API for updating and deleting balance: http://localhost:8000/api/id

Currency Converter API:-

API for exchanging currency from one to another form: http://localhost:8000/currency/

TestCase for user registraion is created which can be checked by "python manage.py test"
