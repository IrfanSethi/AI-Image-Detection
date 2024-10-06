import cv2
import os


vid = cv2.VideoCapture(0)
vid.set(3,800)
vid.set(4,800)

frame_rate = 2  # Desired frame rate (1 frame every 0.5 seconds)
frame_count = 15

output_directory = f"Webcam_frames"
os.makedirs(output_directory, exist_ok=True)


while(True):
    #inside infinity loop
    ret, frame = vid.read()
    cv2.imshow('frame', frame)

    if frame_count % 15 == 0:
        output_file = f"{output_directory}/img_{frame_count}.jpg"
        cv2.imwrite(output_file, frame)
        print(f"Frame {frame_count} has been extracted and saved as {output_file}")

        cv2.waitKey(1)
        if frame_count == 7005:
            break


    frame_count += 15
    print(frame_count)


vid.release()
# Destroy all the windows
cv2.destroyAllWindows() 