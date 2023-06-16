#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16

def callback1(data1):
    rospy.loginfo("Servo1")
    rospy.loginfo(data1.data)
    

def callback2(data2):
    rospy.loginfo("Servo2")
    rospy.loginfo(data2.data)

def callback3(data3):
    rospy.loginfo("Servo3")
    rospy.loginfo(data3.data)

def callback4(data4):
    rospy.loginfo("Servo4")
    rospy.loginfo(data4.data)

def callback5(data5):
    rospy.loginfo("Servo5")
    rospy.loginfo(data5.data)

def callback6(data6):    
    rospy.loginfo("Servo6")
    rospy.loginfo(data6.data)


def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("Servo1", UInt16, callback1)
    rospy.Subscriber("Servo2", UInt16, callback2)
    rospy.Subscriber("Servo3", UInt16, callback3)
    rospy.Subscriber("Servo4", UInt16, callback4)
    rospy.Subscriber("Servo5", UInt16, callback5)
    rospy.Subscriber("Servo6", UInt16, callback6)

    rospy.spin()

if __name__ == '__main__':
    listener()
