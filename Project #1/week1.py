import os
import cv2
import random

vid = cv2.VideoCapture(0)
vid.set(3,800)
vid.set(4,800)

frame_rate = 2  # Desired frame rate (1 frame every 0.5 seconds)
frame_count = 15
startingframe = 15

output_directory = f"Webcam_frames"
os.makedirs(output_directory, exist_ok=True)

#'''
while(True):
    #inside infinity loop
    ret, frame = vid.read()

    if frame_count % 15 == 0:
        output_file = f"{output_directory}/img_{frame_count}.jpg"
        cv2.imwrite(output_file, frame)
        print(f"Frame {frame_count} has been extracted and saved as {output_file}")

        cv2.waitKey(1)

    imgpath = f"Z:\Workshop\Project #1\Webcam_frames\img_{startingframe}.jpg"
    jPath = r"Z:\Workshop\Project #1\vision_creds.json"

    def google_auth(pathJson):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = jPath

    myImage = cv2.imread(imgpath, 1)
    height, width, layers = myImage.shape

    def localize_objects(path):

        from google.cloud import vision

        client = vision.ImageAnnotatorClient()

        with open(path, "rb") as image_file:
            content = image_file.read()
        image = vision.Image(content=content)

        objects = client.object_localization(image=image).localized_object_annotations
        listObject = []

        for object_ in objects:
            curObjDict = {}
            curObjDict["Name"] = object_.name
            curObjDict["ConfidenceScr"] = object_.score
            listCoords = []

            for vertex in object_.bounding_poly.normalized_vertices:

                xVertex = int((vertex.x)*width)
                yVertex = int((vertex.y)*height)
                #curObjDict["Coords"] = (xVertex, yVertex)
                listCoords.append((xVertex, yVertex))

            curObjDict["Coords"] = listCoords
            listObject.append(curObjDict)

        return listObject

    #Authenticate Google
    google_auth(jPath)

    outputData = localize_objects(imgpath)
    for object in outputData:
        print(object, startingframe)
        CurrentConf = object["ConfidenceScr"] 

        if CurrentConf < 0.6:
            continue
        
        ObjCoordsx = object["Coords"][0]
        ObjCoordsy = object["Coords"][2]

        TextCoords = object["Coords"][0]
        TextName = object["Name"]

        print("-------------------------")
        myImage = cv2.rectangle(myImage, ObjCoordsx, ObjCoordsy, (0, 0, 170), 2)

        myImage = cv2.putText(myImage, TextName, TextCoords, cv2. FONT_HERSHEY_SIMPLEX ,0.6, (0, 0, 170), 1, cv2.LINE_AA)

    listOfBoxes = []

    cv2.imshow("Visual Window", myImage)
    cv2.waitKey(10)

    startingframe = startingframe + 15

    frame_count += 15
    print(frame_count)
#'''
