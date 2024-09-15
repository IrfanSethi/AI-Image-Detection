import os
imgpath = r"Z:\Workshop\Project #1\dog_bike_car.jpg"
jPath = r"Z:\Workshop\Project #1\vision_creds.json"


def google_auth(pathJson):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = jPath


def localize_objects(path):
    """Localize objects in the local image.

    Args:
    path: The path to the local file.
    """
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations

    print(f"Number of objects found: {len(objects)}")
    for object_ in objects:
        print(f"\n{object_.name} (confidence: {object_.score})")
        print("Normalized bounding polygon vertices: ")
        for vertex in object_.bounding_poly.normalized_vertices:
            print(f" - ({vertex.x}, {vertex.y})")
    return objects


#Authenticate Google
google_auth(jPath)

outputData = localize_objects(imgpath)

listOfBoxes = []
for item in outputData:
    
    currentItem_BoundingPoly = item.bounding_poly
    print(currentItem_BoundingPoly.normalized_vertices[0].x)


    print("___________________________________")