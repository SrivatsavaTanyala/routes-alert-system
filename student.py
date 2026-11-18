class SMS:
    def __init__(self, student, route):
        self.student = student
        self.route = route
    def send(self, delay):
        return f"SMS: {self.route} delayed by {delay} minutes!"
class Email:
    def __init__(self, student, route):
        self.student = student
        self.route = route
    def send(self, delay):
        return f"Email: {self.route} delayed by {delay} minutes!"
class Student:
    def __init__(self, name, route):
        self.name = name
        self.route = route
        self.inbox = []
    def update(self, message):
        self.inbox.append(message)
    def check_inbox(self):
        return self.inbox