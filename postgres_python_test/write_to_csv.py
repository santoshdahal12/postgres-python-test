"""A module that writes to csv file"""
import csv
from datetime import datetime


def write_to_csv():
    """writes to csv file"""
    fields = ['user_id', 'username', 'email', 'created_on']
    rows = []
    for i in range(1000000):
        rows.append([i, f'test_{i}', f'test_{i}@email.com', f'{datetime.now()}'])
    file_name = "users.csv"
    with open(file_name, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerows(rows)
