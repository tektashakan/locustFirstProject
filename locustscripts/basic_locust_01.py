
from locust import User,task,between

class MyUser(User):

    wait_time=between(10,22)
    #host = "https://www.hepsiburada.com/siparislerim"

    @task
    def login_URL (self):
        print("I am loggin into URL abece")

