import sqlite3
import datetime


DB_NAME = 'FaceBase.db'
conn = sqlite3.connect(DB_NAME)

conn.execute("CREATE TABLE IF NOT EXISTS AttendanceRegister (ID NUMBER, USN VARCHAR, NAME VARCHAR, DAY1 INT, DAY2 INT, DAY3 INT, DAY4 INT, DAY5 INT, TOTALCLASSES INT, TOTALDAYS INT);")

def getDate():
    #datetime.date.today().strftime("%d");
    c='1'
    return c;  

def update_attendance(id, usn, name, isPresent):
    cursor = conn.execute("SELECT * FROM AttendanceRegister WHERE ID=" + str(id) + ";")

    match = cursor.fetchone()

    if match:
        numDays = match[9];
        if isPresent:
            if numDays == 1:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', day1 = " + str(match[3]) + ", day2 = " + getDate() + ", day3 = -1 , day4 = -1, day5 = -1 , totalClasses = " + str(match[8] + 1) + ", totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
            elif numDays == 2:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', day1 = " + str(match[3]) + ", day2 = " + str(match[4]) + ", day3 = " + getDate() + ", day4 = -1, day5 = -1 , totalClasses = " + str(match[8] + 1) + ", totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
            elif numDays == 3:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', day1 = " + str(match[3]) + ", day2 = " + str(match[4]) + ", day3 = " + str(match[5]) + ", day4 = " + getDate() + ", day5 = -1 , totalClasses = " + str(match[8] + 1) + ", totalDays =  " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
            elif numDays == 4:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', day1 = " + str(match[3]) + ", day2 = " + str(match[4]) + ", day3 = " + str(match[5]) + ", day4 = " + str(match[6]) + ", day5 = " + getDate()  + ", totalClasses = " + str(match[8] + 1) + ", totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
        else:
            if numDays == 1:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', day1 = " + str(match[3]) + ", day2 = " + str(0) + ", day3 = -1 , day4 = -1, day5 = -1 , totalClasses = " + str(match[8] ) + ", totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
            elif numDays == 2:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', day1 = " + str(match[3]) + ", day2 = " + str(match[4]) + ", day3 = " + str(0) +", day4 = -1, day5 = -1 , totalClasses = " + str(match[8]) + ",totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
            elif numDays == 3:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', day1 = " + str(match[3]) + ", day2 = " + str(match[4]) + ", day3 = " + str(match[5]) + ", day4 = " + str(0) + ", day5 = -1 , totalClasses = " + str(match[8]) + ", totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")
            elif numDays == 4:
                conn.execute("UPDATE AttendanceRegister SET ID = "+ str(id) + ", usn = '" + usn + "', name = '" + name + "', day1 = " + str(match[3]) + ", day2 = " + str(match[4]) + ", day3 = " + str(match[5]) + ", day4 = " + str(match[6]) + ", day5 = " + str(0)  + ", totalClasses =" + str(match[8]) + ", totalDays = " + str(match[9] + 1) + " WHERE ID = " + str(match[0]) + ";")

    else:
        if isPresent:
            conn.execute("INSERT INTO AttendanceRegister VALUES (" + str(id) + ", '" + usn + "', '" + name + "', '" + getDate() + "', -1 , -1 , -1, -1 ," + str(1) + ", " + str(1) + " );")
        else:
            cursor1 = conn.execute("SELECT * FROM AttendanceRegister ;")
            match = cursor1.fetchone()
            print match
            if match:
                 numDays1 = match[9]
                 if numDays1 == 1:
                     conn.execute("UPDATE AttendanceRegister SET ID = "+ str(match[0]) + ", usn = '" + str(match[1]) + "', name = '" + str(match[2]) + "', day1 = " + str(match[3]) + ", day2 = 0, day3 = -1 , day4 = -1, day5 = -1 , totalClasses = " + str(match[8]) + ", totalDays = " + str(match[9] + 1) + " WHERE id = " + str(match[0]) + ";")
                 elif numDays1 == 2:
                     conn.execute("UPDATE AttendanceRegister SET ID = "+ str(match[0]) + ", usn = '" + str(match[1]) + "', name = '" + str(match[2]) + "', day1 = " + str(match[3]) + ", day2 = " + str(match[4]) + ", day3 = 0 , day4 = -1, day5 = -1 , totalClasses = " + str(match[8]) + ", totalDays = " + str(match[9] + 1) + " WHERE id = " + str(match[0]) + ";")
                 elif numDays1 == 3:
                     conn.execute("UPDATE AttendanceRegister SET ID = "+ str(match[0]) + ", usn = '" + str(match[1]) + "', name = '" + str(match[2]) + "', day1 = " + str(match[3]) + ", day2 = " + str(match[4]) + ", day3 = " + str(match[5]) + " , day4 = 0, day5 = -1 , totalClasses = " + str(match[8]) + ", totalDays = " + str(match[9] + 1) + " WHERE id = " + str(match[0]) + ";")
                 elif numDays1 == 4:
                     conn.execute("UPDATE AttendanceRegister SET ID = "+ str(match[0]) + ", usn = '" + str(match[1]) + "', name = '" + str(match[2]) + "', day1 = " + str(match[3]) + ", day2 = " + str(match[4]) + ", day3 = " + str(match[5]) + " , day4 = " + str(match[5]) + ", day5 = 0 , totalClasses = " + str(match[8]) + ", totalDays = " + str(match[9] + 1) + " WHERE id = " + str(match[0]) + ";")
                #conn.execute("INSERT INTO att_reg VALUES ("+ str(id) + ", '" + usn + "', '" + name + "', " + str(0) + ", -1 , -1 , -1, -1 ," + str(0) + ", " + str( 1) + " );")

    conn.commit()
