import csv
import MySQLdb
import os

mydb = MySQLdb.connect(host="localhost", user="root", passwd="root", db="siren_database")  
cursor = mydb.cursor()
firstline = True
with open(os.path.join('.', 'sb_new.csv'), 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        if firstline:
            firstline = False
            continue
            # name                      = row[0]
            # branch                   = row[1]
            # state                = row[2]
            # city                  = row[3]
            # address                = row[4]
            # zipcode                  = row[5]
            # longitude                = row[6]
            # latitude                    = row[7]
            # phone                    = row[8]

            # cursor.execute('INSERT INTO docs(name,branch,state,city,address,zipcode,longitude,latitude,phone) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', row)
            cursor.execute('INSERT INTO suppliers (name,branch,state,city,address,zipcode,longitude,latitude,phone) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)', (name,branch,state,city,address,zipcode,longitude,latitude,phone))
            break