# time_worked2.py 
# 
# This program calculates the total hours worked on a project
# 
import time
from datetime import datetime

job_log = {}

def enter_info():
    entry1 = input("Job No.: ")
    entry2 = input("Description: ")
    start_time = datetime.now()
    time.sleep(5)
    end_time = datetime.now()
    job_log[entry1] = {"description": entry2, "start": start_time, "end": end_time}
    
def display_entries():
    print(job_log)