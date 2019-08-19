# Imports trend-data.csv into the trendreport_trend table.
# TO RUN: python setup-database.py

import MySQLdb
import os
import sys
import django
import datetime
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'p10.settings')
django.setup()

db = MySQLdb.connect(
    host="127.0.0.1",
    user="trend_report",
    passwd="p102017",
    db="trend_report",
    use_unicode=True
)
cur = db.cursor()
db.autocommit(on=True)

now = timezone.now()

# ----------------------------
# Empty Database
# ----------------------------
if len(sys.argv) == 2:
    print("\nSetting up empty database.\n")
    query = 'DROP DATABASE IF EXISTS trend_report'
    cur.execute(query)
    query = 'CREATE DATABASE trend_report'
    cur.execute(query)
    os.system(sys.argv[1] + " manage.py makemigrations trendreport")
    os.system(sys.argv[1] + " manage.py migrate")
    print("\nCreating default user account\n")
    os.system(sys.argv[1] + " manage.py createsuperuser")
else:
    print("Please run python setup-database.py [py/python/python3]")
    print("py/python/python3 depends on what system you are using.")
    exit(0)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'p10.settings')
django.setup()

db = MySQLdb.connect(
    host="127.0.0.1",
    user="trend_report",
    passwd="p102017",
    db="trend_report",
    use_unicode=True
)
cur = db.cursor()
db.autocommit(on=True)

now = timezone.now()

print("\nStarting import script...\n")

# ----------------------------
# Import some audience members
# ----------------------------

audiences = ["Staff", "Student", "Educator", "Researcher", "External Partner"]

try:
    for x in range(len(audiences)):
        query = "INSERT INTO trendreport_audiencemember(created_date, modified_date, name) VALUES (%s, %s, %s)"
        cur.execute(query, (now, now, audiences[x]))

    print("Successfully imported all audience members!")
except Exception as e:
    print(e)
    print("WARNING: There was an error importing the audience members. You've probably already imported them all. Check the trendreport_audiencemember table.\n")

# --------------------------------------------------
# Import trends from the file Jim originally created
# --------------------------------------------------

f = open("default_data/trend-data.csv")
header = f.readline()
default_image = "default.jpg"
try:
    for line in f.readlines():
        trend = line.split('|')
        data = [None for x in range(7)]
        for i in range(len(trend)):
            if trend[i]:
                attr = trend[i].strip()
                data[i] = attr.strip("\"")
        if trend[6] is None:
            trend[6] = default_image

        query = "INSERT INTO trendreport_trend(created_date, modified_date, name, description, short_description, importance, howToProceed, examples, background) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(query, (now, now, data[0], data[1], data[2], data[3], data[4], data[5], data[6]))

    print("Successfully imported all trends!")
except Exception as e:
    print(e)
    print("WARNING: There was an error importing the trends. You've probably already imported them all. Check the trendreport_trend table.\n")
f.close()

# -----------------------------------------
# Import projects from Sonya's project list
# -----------------------------------------

f = open("default_data/project-data.csv")
header = f.readline()
default_image = "default.jpg"
try:
    for line in f.readlines():
        project = line.split('|')
        data = [None for x in range(4)]
        for i in range(len(project)):
            if project[i]:
                attr = project[i].strip()
                data[i] = attr.strip("\"")
        if data[2] is None:
            data[2] = data[1][:128]
        if data[3] is None:
            data[3] = default_image

        query = "INSERT INTO trendreport_project(created_date, modified_date, name, description, short_description, background) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(query, (now, now, data[0], data[1], data[2], data[3]))

    print("Successfully imported all projects!")
except Exception as e:
    print(e)
    print("WARNING: There was an error importing the projects.\n")
f.close()

# -----------------------------------------
# Import Principles from principles-data.csv
# -----------------------------------------

f = open("default_data/principles-data.csv")
header = f.readline()
try:
    for line in f.readlines():
        principle = line.split('|')
        data = [None for x in range(3)]
        for i in range(len(principle)):
            if principle[i]:
                attr = principle[i].strip()
                data[i] = attr.strip("\"")

        query = "INSERT INTO trendreport_principle(created_date, modified_date, name, description, icon) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (now, now, data[0], data[1], data[2]))

    print("Successfully imported all principles!")
except Exception as e:
    print(e)
    print("WARNING: There was an error importing the principles. You've probably already imported them all. Check the principles table.\n")
f.close()
# ---------
# Finished!
# ---------

# -----------------------------------------
# Import Admin data from admin-data.csv
# -----------------------------------------

f = open("default_data/admin-data.csv")
header = f.readline()
try:
    for line in f.readlines():
        admin = line.split('|')
        data = [None for x in range(3)]
        for i in range(len(admin)):
            if admin[i]:
                attr = admin[i].strip()
                data[i] = attr.strip("\"")

        query = "INSERT INTO trendreport_admin(name, description, image) VALUES (%s, %s, %s)"
        cur.execute(query, (data[0], data[1], data[2]))

    print("Successfully imported all admin data!")
except Exception as e:
    print(e)
    print("WARNING: There was an error importing the admin data. You've probably already imported it all. Check the admin table.\n")
f.close()
# ---------
# Finished!
# ---------


db.close()
print("\nLooks like I'm finished! Check your trendreport database.\n")
