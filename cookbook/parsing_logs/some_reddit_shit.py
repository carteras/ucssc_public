from pathlib import Path
from datetime import datetime

log_file = "D:/github/ucssc/cookbook/parsing_logs/log"

class Employee:
    def __init__(self, id):
        self.id = id
        self.in_time = None
        self.out_time = None

    def log_action(self, time_stamp, action):
        if action == "log-in":
            self.in_time = time_stamp
        elif action == "log-out":
            self.out_time = time_stamp

    def get_time_at_work(self):
        return f"{self.id} worked {self.out_time - self.in_time}"

employees = {}

with open(log_file) as read_in:
    for line in read_in.readlines():
        time_stamp, uid, action = line.split()
        uid = uid[1:len(uid)-1]
        time_stamp = datetime.strptime(time_stamp, "%H:%M:%S")
        if uid not in employees.keys():
            employees[uid] = Employee(uid)
        employees[uid].log_action(time_stamp, action)
        
for employee in employees:
    print(employees[employee].get_time_at_work())
        