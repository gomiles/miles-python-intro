# Task Description:
# This exercise focuses on managing maintenance schedules for power system operations,
# a critical task for professionals such as engineers and supervisors in the energy sector.
# You will work with a CSV file named 'maintenance_schedule.csv' that contains maintenance
# task data with three columns: Task_Name (e.g., "Transformer Check"), Due_Date (in YYYY-MM-DD format),
# and Status (e.g., "Completed", "Pending"). The goal is to identify and report
# all maintenance tasks that are overdue as of today, May 20, 2025, 11:54 PM CEST.
# A task is considered overdue if its Due_Date is earlier than today and its Status is not "Completed".
# This is a practical application for real-time operation and maintenance planning, relevant
# to roles like Senior Engineer - Real Time Operation and Engineer - Telecom & OTS Maint & Commg.
#
# Steps to Complete:
# 1. Import the required modules: 'csv' for reading the CSV file and 'datetime' for date handling.
# 2. Open and read the 'maintenance_schedule.csv' file, skipping the header row.
# 3. Set today's date to May 20, 2025, for comparison (time can be ignored for this exercise).
# 4. Iterate through each row in the CSV file.
# 5. Convert the Due_Date string (e.g., "2025-05-10") to a datetime object using strptime.
# 6. Check if the task is overdue by comparing Due_Date with today and verifying Status is not "Completed".
# 7. Print detailed information about each overdue task, including Task_Name, Due_Date, and Status.
# 8. Test the script with the provided CSV data to ensure it correctly identifies overdue tasks.

import csv
from datetime import datetime

# Define today's date (May 20, 2025) for comparison
today = datetime(2025, 5, 20)

