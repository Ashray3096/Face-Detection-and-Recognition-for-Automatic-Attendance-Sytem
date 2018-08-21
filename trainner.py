import cv2, os

# Import numpy for matrix calculation
import numpy as np

# Import Python Image Library (PIL)
from PIL import Image

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Using prebuilt frontal face training model, for face detection
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# Create method to get the images and label data
def getImagesAndLabels(path):

    # Get all file path
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
    
    # Initialize empty face sample
    faceSamples=[]
    
    # Initialize empty id
    ids = []

    # Loop all the file path
    for imagePath in imagePaths:
     

        # Get the image and convert it to grayscale
        PIL_img = Image.open(imagePath).convert('L')

        # PIL image to numpy array
        img_numpy = np.array(PIL_img,'uint8')

        # Get the image id
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        print id
        # Get the face from the training images
        faces = detector.detectMultiScale(img_numpy)

        # Loop for each face, append to their respective ID
        for (x,y,w,h) in faces:

            # Add the image to face samples
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            
            # Add the ID to IDs
            ids.append(id)
            cv2.imshow("trainning",img_numpy[y:y+h,x:x+w])
            cv2.waitKey(10)
    # Pass the face array and IDs array
    return faceSamples,ids

# Get the faces and IDs
faceSamples,ids = getImagesAndLabels('dataset')
cv2.imshow('test',faceSamples[0])
cv2.waitKey(1)
# Train the model using the faces and IDs
recognizer.train(faceSamples, np.array(ids))

# Save the model into trainer.yml
recognizer.write('trainer/trainer.yml')
cv2.destroyAllWindows()

