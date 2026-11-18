from observer import Observer
class Route:
    def __init__(self, name):
        self.name = name
        self.observer = Observer()
    def subscribe(self, student, alert_type):
        self.observer.subscribe(student, alert_type)
    def report_delay(self, delay):
        if delay >= 10:
            self.observer.notify(self.name, delay)