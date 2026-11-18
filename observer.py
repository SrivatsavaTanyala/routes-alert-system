from student import SMS, Email
class Observer:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, student, alert_type):
        self.subscribers.append((student, alert_type))
    def notify(self, route, delay):
        for student, alert_type in self.subscribers:
            if student.route == route:
                if alert_type == "SMS":
                    alert = SMS(student, route)
                else:
                    alert = Email(student, route)
                student.update(alert.send(delay))