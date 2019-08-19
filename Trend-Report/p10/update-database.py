import os
import sys

if len(sys.argv) == 2:
    print("\nRunning migrations.\n")
    os.system(sys.argv[1] + " manage.py makemigrations trendreport")
    os.system(sys.argv[1] + " manage.py migrate")
    print("\nShowing Migrations\n")
    os.system(sys.argv[1] + " manage.py showmigrations")
else:
    print("Please run python update_database.py [py/python/python3]")
    print("py/python/python3 depends on what system you are using.")
    exit(0)
