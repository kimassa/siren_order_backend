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
cursor.execute(f"DELETE FROM suppliers")

with open('sb_new.csv', encoding='utf-8-sig') as csv_files:
    reader = csv.DictReader(csv_files)

    for row in reader:
        print(row)

        
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
            {row['kim']},
            {row['branch']},
            {row['state']},
            {row['city']},
            {row['address']},
            {row['zipcode']},
            {row['longitude']},
            {row['latitude']},
            {row['phone']}
            )"""

        cursor.execute(sql)


db.commit()
db.close()