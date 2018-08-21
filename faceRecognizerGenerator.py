import cv2
import sqlite3
# Import numpy for matrices calculations
import numpy as np
import database

i = 0
n = "null"
u = "null"
# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

def getProfile(Id):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM RegisteredUsers WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile = row
        #conn.close()
    return profile

def insertOrUpdate(face_id,face_name):
    print face_id
    print face_name
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM Attendance WHERE ID="+str(face_id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist == 1):
        cmd="UPDATE Attendance SET Name = "+face_name+"WHERE ID="+face_id
    else:
        cmd="INSERT INTO Attendance VALUES('"+str(face_id)+"','"+face_name+"','Present')"
    conn.execute(cmd)
    conn.commit()
    #cam.release();
    #conn.close()

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

# Loop
while True:
    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Recognize the face belongs to which ID
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
        if conf < 70:
            profile = getProfile(Id)
       
            if(profile != None):
         
        # Put text describe who is in the picture
                cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
                cv2.putText(im, str(profile[1]), (x,y-40), font, 2, (255,255,255), 3)
                i =profile[0]
                n =str(profile[1])
                u =str(profile[2])
        else:
              cv2.putText(im, "Unknown", (x,y-40), font, 2, (255,255,255), 3)
    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 
            
    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

        
# Stop the camera
cam.release()
# Close all windows
cv2.destroyAllWindows()
print i
if(i == 0):
        td = raw_input('Enter total number of Days passed to update absentees')
        DB_NAME = 'FaceBase.db'
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.execute("Select totalDays from AttendanceRegister");
        match = cursor.fetchall()
        if(td == '2'):
            for record in match:
                if record == (1,):
                    conn.execute("update  AttendanceRegister set day2=0 ,totalDays=2 WHERE totalDays =1 ");
                    print "Successfully Updated!"
                    conn.commit()
        if(td == '3'):
            for record in match:
                if record == (2,):
                    conn.execute("update  AttendanceRegister set day3=0 ,totalDays=3 WHERE totalDays =2 ");
                    print "Successfully Updated!"
                    conn.commit()
        if(td == '4'):
            for record in match:
                if record == (3,):
                    conn.execute("update  AttendanceRegister set day4=0 ,totalDays=4 WHERE totalDays =3 ");
                    print "Successfully Updated!"
                    conn.commit()
        if(td == '5'):
            for record in match:
                if record == (4,):
                    conn.execute("update  AttendanceRegister set day5=0 ,totalDays=5 WHERE totalDays =4 ");
                    print "Successfully Updated!"
                    conn.commit()   
                        
else:
        database.update_attendance(i, u, n, True)


