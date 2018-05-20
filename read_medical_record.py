import MySQLdb as sql
import sys

def read_data(id):
    
    # print "the id coming is "+id
    
    db = sql.connect('localhost', 'root', 'nodejs', 'medical_information')
    if(db):
        # print "successfully connected to the database"
        pass
    else:
        # print "cannot connect to the database successfully"
        pass
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM info;")
        data = cursor.fetchone()
        return data
    except db.error as e:
        pass 
        # print(e)
        # print "cannot read from the database"
    
    cursor.close()

    db.close()

if len(sys.argv) > 1: 
    imgNo = sys.argv[1]
    read_data(imgNo)