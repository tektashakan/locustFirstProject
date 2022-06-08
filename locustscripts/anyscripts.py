from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 8)
    host="https://api.openbrewerydb.org"

    @task
    def index_page(self):
        self.client.get("/breweries")
