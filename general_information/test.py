import json
import random
import MySQLdb as sql

with open('name_and_sex.json') as file:
    data = json.load(file)
    names = data.keys()
    sexs = data.values()

    age = []
    for i in range(0, 400):
        age.append(random.randint(20, 60))

    print age

    db = sql.connect('localhost', 'root', 'nodejs', 'medical_information')
    if(db):
        # print "successfully connected to the database"
    else:
        print "cannot connect to the database successfully"
    cursor = db.cursor()

    # for i in range(0, 399):
    #     query = "insert into info(name, age, sex, medical_history) values('{}', '{}', 'female', 'no medical history found');".format(names[i], age[i])

    #     try:
    #         cursor.execute(query)
    #         db.commit()
    #         print "done entering the content into database"
    #     except:
    #         print "cannot enter into database"
    #         db.rollback()

    read_data = []

    for i in range(0, 399):
        query = "select * from info"

        try:
            cursor.execute(query)
            db.commit()
            print "done reading the content from database"
            print(cursor.fetchone())
            read_data.append(cursor.fetchone())
        except:
            print "cannot fetch the data from the database"
            db.rollback()

    db.close()
