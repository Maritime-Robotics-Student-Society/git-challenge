import rosbag
import rospy

"""
Small example how to analyse a rosbag
We are trying to find out where we first detected the obstacle!
"""


extravaganzaBag = rosbag.Bag("extravaganza.bag")
message_stream = iter(extravaganzaBag.read_messages():
    
