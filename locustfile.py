from locust import HttpUser, task, between

class WebsiteUser(HttpUser):

    wait_time = between(1, 5)

    @task(1)  # Task weight of 1; this will be executed the most
    def load_homepage(self):
        self.client.get("/")

    @task(2)  # Task weight of 2; this will run twice as often as load_homepage
    def load_testing_page(self):
        self.client.get("/software-testing")

    @task(1)
    def load_services_page(self):
        self.client.get("/services")

    @task(1)
    def load_contact_page(self):
        self.client.get("/contact")


# locust --host=https://tezzasolutions.com
