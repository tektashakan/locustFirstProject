
from locust import HttpUser,task,between

class MyUser(HttpUser):

    wait_time=between(1,2)
    host = "https://www.hepsiburada.com/siparislerim"
    #host belirtirsen host alanında otomatik setler belirtmezse istek atarken de belirtebilirsin
    #locust -f locustscripts/basic_http_host01.py --host="http://newtours.demoaut.com/"


    @task
    def login_URL (self):
        print("I am loggin into URL abece")

