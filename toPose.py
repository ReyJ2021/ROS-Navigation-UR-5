#!/usr/bin/env python3

import rospy
import numpy as np
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

# def move_to_pose(pose2):
#     path = Path()


#     pose = PoseStamped()
#     pose.pose.orientation.w = 0.0
#     pose.pose.orientation.x =0.0
#     pose.pose.orientation.y = 0.0
#     pose.pose.orientation.z = 0.0
#     pose.pose.position.x = 5.2
#     pose.pose.position.y = 6.4
#     pose.pose.position.z = 5.5
#     path.poses.append(pose)
#     path.poses.append(pose2)
    

#    # print(path)

#     rospy.sleep(0.5)
#     pub.publish(path)
#     rospy.sleep(0.5)
#     return path

# rospy.init_node('move_to_pose')
# pub = rospy.Publisher('/trajectory_planned', Path, queue_size=1)
# sub = rospy.Subscriber('/controller_ur/move_to_pose', PoseStamped, move_to_pose)



# rospy.spin()


def move_to_pose(pose2):
    pose = PoseStamped()
    # if pose2.shape[0] == 0:
    #     return path
    # pose2 = pose2[0]

    
    pose.header.frame_id = "velodyne"
    pose.pose.orientation.x = 0.1 
    pose.pose.orientation.y = 0.1 
    pose.pose.orientation.z = 0.1 
    pose.pose.orientation.w = 0.1 

    pose.pose.position.x = 3.5
    pose.pose.position.y = 4.5
    pose.pose.position.z = 5.5

    pose.header.seq = path.header.seq + 1
    pose.header.frame_id = "velodyne"

    path.header.stamp = rospy.Time.now()
    pose.header.stamp = path.header.stamp

    path.poses.append(pose)
    path.poses.append(pose2)

    rospy.sleep(0.5)
    pub.publish(path)
    rospy.sleep(0.5)

def callback(data):
    move_to_pose(data)

if __name__ == "__main__":
    rospy.init_node('move_to_pose', anonymous=True)

    path = Path()
    pub = rospy.Publisher('/trajectory_planned', Path, queue_size=1)
    pub.publish(path)
    print(path)
    sub = rospy.Subscriber('/controller_ur/move_to_pose', PoseStamped, callback)

    rospy.spin()
    
