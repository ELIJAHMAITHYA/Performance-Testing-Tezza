from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Simulate a wait time between requests

    @task
    def load_homepage(self):
        self.client.get("/")

    @task
    def load_testing_page(self):
        self.client.get("/software-testing")

    @task
    def load_services_page(self):
        self.client.get("/services")  #

    @task
    def load_contact_page(self):
        self.client.get("/contact")
