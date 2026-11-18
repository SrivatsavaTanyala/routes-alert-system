import unittest
from student import Student
from routes import Route
class TestRoutes(unittest.TestCase):
    def test_alerts(self):
        for delay, expected in [(9, 0), (10, 1)]:
            r = Route("Warangal")
            s = Student("Rahul", "Warangal")
            r.subscribe(s, "SMS")
            r.report_delay(delay)
            self.assertEqual(len(s.check_inbox()), expected)
if __name__ == "__main__":
    unittest.main()