import os
from locust import HttpUser, TaskSet, task, between
from bs4 import BeautifulSoup


class CCLUser(HttpUser):
    wait_time = between(1, 5)  # Simula un tempo di attesa tra 1 e 5 secondi
    host = os.getenv("LOCUST_HOST", "http://localhost")
    
    @task
    def view_home(self):
        self.client.get("/")
    
    @task
    def view_health_db(self):
        self.client.get("/health-db")
    
    @task
    def view_user_list(self):
        self.client.get("/users")
        
    @task
    def read_first_user(self):
        self.client.get("/users/1")
        
    @task
    def read_first_user(self):
        self.client.get("/users/2") 