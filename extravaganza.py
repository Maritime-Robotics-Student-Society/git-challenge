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

# Here is my my version of this script.
# It took me a little while to work out how to access and compare the messages.
# I get a slightly different result to the above script as I am taking the position immediatly before
# the detection and the above script is taking the position immediatly after the detection.

extravaganza_bag = rosbag.Bag('extravaganza.bag')
position = None

for topic, msg, t in extravaganza_bag.read_messages(topics=['/camera_detection', '/position']):
    if topic == '/position':
        position = msg
    elif msg.data == 'detected':
        print ('First detection at latitude:{} longitude:{}'.format(position.latitude, position.longitude))
        break
else:
    print('Detection event not found')

    
