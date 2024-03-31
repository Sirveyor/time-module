# time_worked.py
"""
Module to log the time worked on a project.
"""
import datetime
import json

class TimeLog:
    """Creates the time log"""

    def __init__(self):
        self.time_logs = []


    def add_log(self, project_number, description, start_datetime, end_datetime):
        """ Create a dictionary to hold time log"""
        time_log = {
            'project_number': project_number,
            'description': description,
            'start_datetime': start_datetime,
            'end_datetime': end_datetime
        }
        self.time_logs.append(time_log)

    def print_logs(self, filename='time_logs.json'):
        """ Temporary function to print time log.
            Will be replaced with a gui
        """


        for log in self.time_logs:
            #print("Project Number: {}\nDescription: {}\nStart Time: {}\nEnd Time: {}\n".format(
               # log['project_number'], log['description'], log['start_datetime'], log['end_datetime']))
            msg = (
                f"Project Number: {log['project_number']}\n" +
                f"Description:  {log['description']}\n" +
                f"Start Time: {log['start_datetime']}\n" +
                f"End Time:  {log['end_datetime']}\n"
                )
            print(msg)

# Get user inputs
project_number = input("Enter Project Number: (or q to quit)\n")
description = input("Enter Description of Work: ")
start_datetime = datetime.datetime.now()
# Add a small delay to simulate work time
start_datetime += datetime.timedelta(seconds=10)
end_datetime = datetime.datetime.now()

# Create TimeLog object and add to the log
time_log = TimeLog()
time_log.add_log(project_number, description, str(start_datetime), str(end_datetime))
# Print the log
time_log.print_logs()
