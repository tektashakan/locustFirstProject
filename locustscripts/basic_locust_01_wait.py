
from locust import User,task,between,constant,constant_pacing
from datetime import datetime

class MyUser(User):

    #wait_time=between(10,30) #10 ile 30 saniye arasında istek atar
    #wait_time=constant(15) #15 saniye de bir istek atar
    wait_time=constant_pacing(9) #9 saniyede bir hıza bağlı olarak istek atar
    host = "https://api.openbrewerydb.org"
    @task
    def login_URL (self):
        print(datetime.now())



