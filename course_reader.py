__author__ = 'sk9gn'


import csv
import sqlite3


# read from CSV file and load into database table
def load_course_database(db_name, csv_filename):
    with open(csv_filename, 'rU') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                conn = sqlite3.connect(db_name)
                with conn:
                    cur = conn.cursor()
                    tup = tuple(row)
                    sql_cmd = "insert into coursedata values(?, ?, ?, ?, ?, ?, ?)"
                    cur.execute(sql_cmd, tup)


if __name__ == '__main__':
    load_course_database("course1.db", "seas-courses-5years.csv")