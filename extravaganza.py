import rosbag
import rospy

"""
Small example how to analyse a rosbag
We are trying to find out where we first detected the obstacle!
"""

extravaganzaBag = rosbag.Bag("extravaganza.bag")
for topic, msg, t in extravaganzaBag.read_messages():
    if topic == "/camera_detection":
        if msg.data == "detected":
            detectionTime = t
            break

for topic, msg, t in extravaganzaBag.read_messages():
    if topic == "/position":
        if t > detectionTime:
            timeReached = True
            print("The position of the boat when an obstacle was detected was: \n"
                +"Latitude: " + str(msg.latitude) + "\nLongitude: " + str(msg.longitude))
            break


    
