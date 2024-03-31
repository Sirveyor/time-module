# time_worked2.py
#
# This program calculates the total hours worked on a project
#
import os
from datetime import datetime
import json

job_log = {}


def enter_info():
    """
        Function to get time spent on each job
    """
    entry1 = input("Job No.: ")
    entry2 = input("Description: ")
    start_time = datetime.now()
    input("Press Enter to continue")  # this will be replace with a gui button
    end_time = datetime.now()
    total_time = hours_worked(start_time, end_time)
    job_log[entry1] = {"description": entry2, "start": str(start_time), "end": str(end_time),
                       "total": total_time}
    save_to_file()


def display_entry():
    """
    Displays current entry in the log

    """
    print(f'Current Entry: {job_log}')


def save_to_file():
    """
        Function to save data
    """
    if os.path.exists('job_logs.json'):
        with open('job_logs.json', 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
    else:
        existing_data = {}
    existing_data.update(job_log)

    with open("job_logs.json", 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, indent=4)


def hours_worked(start, end):
    """_summary_

    Args:
        start (datetime): start time on project
        end (datetime): end time on project

    Returns:
        hours (double): hours worked on project
    """
    time_diff = end - start
    total_seconds = time_diff.total_seconds()
    hours = total_seconds / 3600
    return (round(hours, 5), round(hours * 195, 3))

# enter_info()
# display_entry()
