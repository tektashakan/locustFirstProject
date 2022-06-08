
from locust import User,task

class MyUser(User):
    @task
    def login_URL (self):
        print("I am loggin into URL")

