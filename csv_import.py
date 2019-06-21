import csv
import mysql.connector
import my_settings
from django.db import connection

db_settings = my_settings.DATABASES
options = db_settings['default'].get('OPTIONS', None)

if options and 'read_default_file' in options:
    db = mysql.connector.connect(read_default_file=options['read_default_file'])
else:
    db_default = db_settings['default']
    db = mysql.connector.connect(host= db_default.get('HOST'),
                         user= db_default.get('USER'),
                         passwd= db_default.get('PASSWORD'),
                         db= db_default.get('NAME'))

cursor = db.cursor()
# cursor.execute(f"DELETE FROM suppliers")

with open('sb_new.csv', encoding='utf-8-sig') as csv_files:
    reader = csv.DictReader(csv_files)

    for row in reader:
        print(f"--{row['kim']}")
        print(f"--{row['branch']}")
        print(f"--{row['state']}")
        print(f"--{row['city']}")
        print(f"--{row['address']}")
        print(f"--{row['zipcode']}")
        print(f"--{row['longitude']}")
        print(f"--{row['latitude']}")
        print(f"--{row['phone']}")

        sql = f"""INSERT INTO suppliers (
            name,
            branch,
            state,
            city,
            address,
            zipcode,
            longitude,
            latitude,
            phone
        ) VALUES (
            %(kim)s,
            %(branch)s,
            %(state)s,
            %(city)s,
            %(address)s,
            %(zipcode)s,
            %(longitude)s,
            %(latitude)s,
            %(phone)s
        )"""

        cursor.execute(sql, row)


db.commit()

with open('sb_product.csv', encoding='utf-8-sig') as csv_files:
    reader = csv.DictReader(csv_files)

    for row in reader:

        sql = f"""INSERT INTO products (
            menu_type,
            menu_category,
            name,
            drink_size,
            drink_type,
            price
        ) VALUES (
            %(menu_type)s,
            %(menu_category)s,
            %(name)s,
            %(drink_size)s,
            %(drink_type)s,
            %(price)s
        )"""
        cursor.execute(sql, row)

db.commit()
db.close()
