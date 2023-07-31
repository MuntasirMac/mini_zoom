import cv2
import redis

#opening a video capture for webcam
video = cv2.VideoCapture(0)

#Resizing parameters
height = int(video.get(4)/2)
width = int(video.get(3)/2)

#opening a redis connection to be used as publisher
server = redis.Redis()

#while video camera is on
while video.isOpened():

    #read a frame from the camera. Frame is a 2D array of pixels
    ret, frame = video.read()
    if ret:
        frame = cv2.resize(frame, (width, height))

        #publish the frame (message packet) to a channel named user_1
        server.publish("user_1", frame.tobytes())

video.release()