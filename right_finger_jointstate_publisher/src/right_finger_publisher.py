#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
import threading

class RightFingerJointStatePublisher:

    def __init__(self):
        rospy.init_node('right_finger_jointstate_publisher')
        self.lock = threading.Lock()
        self.name = "pg70_finger_left_joint"
        self.pub = rospy.Publisher('joint_states', JointState, queue_size=5)
        self.thread = threading.Thread(target=self.joint_states_listener)
        self.thread.start()
        

    #thread function: listen for joint_states messages
    def joint_states_listener(self):
        rospy.Subscriber('joint_states', JointState, self.joint_states_callback)
        rospy.spin()


    #callback function: when a joint_states message arrives, save the values
    def joint_states_callback(self, msg):
        self.lock.acquire()
        if self.name in msg.name:
            index = msg.name.index(self.name)
            js = JointState()
            js.header.stamp = msg.header.stamp
            js.name = ['pg70_finger_right_joint']
            js.position = [msg.position[index]]
            js.velocity = [msg.velocity[index]]
            js.effort = [msg.effort[index]]     
            #rospy.loginfo("position: %f", self.jointstate.position)   
            self.pub.publish(js)    
        self.lock.release()


if __name__ == '__main__':
    
    rightfingerpublisher = RightFingerJointStatePublisher()
    rospy.loginfo("right_finger_jointstate_publisher started...")

    rospy.spin()
    
    